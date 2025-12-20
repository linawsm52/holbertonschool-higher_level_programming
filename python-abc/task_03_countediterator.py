#!/usr/bin/python3
"""CountedIterator - keeps track of how many items were iterated."""

class CountedIterator:
    """Iterator wrapper that counts how many items have been returned."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration automatically
        self.count += 1
        return item

    def get_count(self):
        return self.count
