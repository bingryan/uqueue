#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from collections import deque

from uqueue import ABCFifoQueue


class FifoQueue(ABCFifoQueue):

    def __init__(self, conn=None, name=None):
        """

        :param conn: redis connect
        """
        self.conn = conn
        self.name = name if name is not None else "uqueue"

    def dequeue(self):
        return self.conn.rpop(self.name)

    def dequeue_many(self, n):
        res = deque(maxlen=n)

        pipe = self.conn.pipeline(transaction=True)
        for _ in range(n):
            res.append(self.conn.rpop(self.name))
        pipe.execute()
        return res

    def enqueue(self, value):
        assert value is not None
        self.conn.lpush(self.name, value)

    def enqueue_many(self, iterable):
        pipe = self.conn.pipeline(transaction=True)
        self.conn.lpush(self.name, *iterable)
        pipe.execute()

    def count(self, value=None):
        if value is None:
            return conn.llen(self.name)
        return conn.lrem(self.name, 0, value)


class LifoQueue(FifoQueue):
    def dequeue(self):
        return self.conn.lpop(self.name)

    def dequeue_many(self, n):
        res = deque(maxlen=n)

        pipe = self.conn.pipeline(transaction=True)
        for _ in range(n):
            res.append(self.conn.lpop(self.name))
        pipe.execute()
        return res


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
    conn = redis.StrictRedis(connection_pool=pool)
    f = FifoQueue(conn)
    f.enqueue("a")
