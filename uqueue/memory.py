#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uqueue import ABCFifoQueue
from collections import deque


class FifoQueue(ABCFifoQueue):
    """ Memory FifoQueue """

    def __init__(self):
        self._q = deque()

    def dequeue(self):
        return self._q.popleft()

    def dequeue_many(self, n):
        res = deque(maxlen=n)
        for _ in n:
            res.appendleft(self._q.popleft())
        return res

    def enqueue(self, value):
        self._q.append(value)

    def enqueue_many(self, iterable):
        self._q.extend(iterable)

    def count(self, value):
        return self._q.count(value)

    def __call__(self):
        return self._q


class LifoQueue(ABCFifoQueue):
    """ Memory LifoQueue """

    def __init__(self):
        self._q = deque()

    def dequeue(self):
        return self._q.pop()

    def dequeue_many(self, n):
        res = deque(maxlen=n)
        for _ in n:
            res.append(self._q.pop())
        return res

    def enqueue(self, value):
        self._q.append(value)

    def enqueue_many(self, iterable):
        self._q.extend(iterable)

    def count(self, value):
        return self._q.count(value)

    def __call__(self):
        return self._q
