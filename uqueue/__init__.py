#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta


class ABCQueue(metaclass=ABCMeta):

    def append(self, *args, **kwargs):  # real signature unknown
        """ Add an element to the right side of the queue. """
        pass

    def appendleft(self, *args, **kwargs):  # real signature unknown
        """ Add an element to the left side of the queue. """
        pass

    def appendright(self, *args, **kwargs):  # real signature unknown
        """ Add an element to the right side of the queue. """
        pass

    def clear(self, *args, **kwargs):  # real signature unknown
        """ Remove all elements from the queue. """
        pass

    def copy(self, *args, **kwargs):  # real signature unknown
        """ Return a shallow copy of a queue. """
        pass

    def count(self, value):  # real signature unknown; restored from __doc__
        """ D.count(value) -> integer -- return number of occurrences of value """
        return 0

    def extend(self, *args, **kwargs):  # real signature unknown
        """ Extend the right side of the queue with elements from the iterable """
        pass

    def extendleft(self, *args, **kwargs):  # real signature unknown
        """ Extend the left side of the queue with elements from the iterable """
        pass

    def extendright(self, *args, **kwargs):  # real signature unknown
        """ Extend the right side of the queue with elements from the iterable """
        pass

    def index(self, value, start=None, stop=None):  # real signature unknown; restored from __doc__
        """
        D.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

    def insert(self, index, p_object):  # real signature unknown; restored from __doc__
        """ D.insert(index, object) -- insert object before index """
        pass

    def pop(self, *args, **kwargs):  # real signature unknown
        """ Remove and return the rightmost element. """
        pass

    def popleft(self, *args, **kwargs):  # real signature unknown
        """ Remove and return the leftmost element. """
        pass

    def remove(self, value):  # real signature unknown; restored from __doc__
        """ D.remove(value) -- remove first occurrence of value. """
        pass

    def reverse(self):  # real signature unknown; restored from __doc__
        """ D.reverse() -- reverse *IN PLACE* """
        pass

    def rotate(self, *args, **kwargs):  # real signature unknown
        """ Rotate the queue n steps to the right (default n=1).  If n is negative, rotates left. """
        pass


class ABCFifoQueue(object):

    """
    FifoQueue class interface

    """

    def dequeue(self, *args, **kwargs):
        """Dequeues one element from this queue"""
        pass

    def dequeue_many(self, *args, **kwargs):
        """Dequeues zero or more element from this queue"""
        pass

    def enqueue(self, *args, **kwargs):
        """Enqueues one element to this queue."""
        pass

    def enqueue_many(self, *args, **kwargs):
        """Enqueues zero or more elements to this queue."""
        pass

    def size(self, *args, **kwargs):
        """Compute the number of elements in this queue."""
        return 0
