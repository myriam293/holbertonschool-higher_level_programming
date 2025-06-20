#!/usr/bin/python3
"""Create a class named CountedIterator that
extends the built-in iterator obtained from the iter function."""


class CountedIterator:
    """The CountedIterator should keep track of the number of items
    that have been iterated over by overriding the __next__ method."""

    def __init__(self, iterable):
        """Initialize the iterator object using iter() and a counter
        to track the number of items iterated."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Increment the counter each time an item is fetched
        and return the next item from the iterator."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter
