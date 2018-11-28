#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import ABCFifoQueue


class FifoQueue(ABCFifoQueue):
    """ Memory FifoQueue """

    _sql_create = """
        CREATE TABLE IF NOT EXISTS uqueue (
          id bigint unsigned NOT NULL AUTO_INCREMENT,
          item blob NOT NULL,
          PRIMARY KEY (id)
        )
    """

    _sql_enqueue = """INSERT INTO uqueue (item) VALUES (?)"""
    _sql_enqueue_many = """INSERT INTO uqueue (item) VALUES {}"""
    _sql_dequeue_select = """SELECT item FROM uqueue ORDER BY id LIMIT {}"""
    _sql_dequeue_delete = 'DELETE FROM uqueue ORDER BY id LIMIT {}'

    _sql_count = """SELECT COUNT(*) FROM uqueue where item = {}"""

    def __init__(self, sql_connection):
        self.connection = sql_connection
        with self.connection.cursor() as cursor:
            cursor.execute(self._sql_create)

    def _dequeue(self, n):
        assert n > 0
        item = None
        try:
            cursor = self.connection.cursor()
            item = cursor.execute(self._sql_dequeue_select.format(n))
            cursor.execute(self._sql_dequeue_delete.format(n))
        except:
            self.connection.rollback()
            self.connection.close()
            print("Oops!  checkout your db connection and try again...")
        else:
            self.connection.commit()
            cursor.close()
            self.connection.close()

        return item

    def dequeue(self):
        return self._dequeue(1)

    def dequeue_many(self, n):
        return self._dequeue(n)

    def enqueue(self, value):
        assert value is not None
        with self.connection.cursor() as cursor:
            cursor.execute(self._sql_enqueue, (value,))

    def enqueue_many(self, iterable):
        values = list(iterable)
        if len(values) < 2:
            return self.enqueue(iterable)
        values_format = "(?),".join(["" for _ in range(len(values))]) + " (?)"

        with self.connection.cursor() as cursor:
            cursor.execute(self._sql_enqueue_many.format(values_format), tuple(values))

    def count(self, value):
        with self.connection.cursor() as cursor:
            return next(cursor.execute(self._sql_count.format(value)))[0]


class LifoQueue(FifoQueue):
    _sql_dequeue_select = """SELECT item FROM uqueue ORDER BY id DESC LIMIT {}"""
    _sql_dequeue_delete = 'DELETE FROM uqueue ORDER BY id DESC LIMIT {}'
