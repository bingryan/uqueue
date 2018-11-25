#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import ABCFifoQueue


class FifoQueue(ABCFifoQueue):
    """ Memory FifoQueue """

    def dequeue(self, *args, **kwargs):
        super().dequeue(*args, **kwargs)

    def dequeue_many(self, *args, **kwargs):
        super().dequeue_many(*args, **kwargs)

    def enqueue(self, *args, **kwargs):
        super().enqueue(*args, **kwargs)

    def enqueue_many(self, *args, **kwargs):
        super().enqueue_many(*args, **kwargs)

    def size(self, *args, **kwargs):
        return super().size(*args, **kwargs)
