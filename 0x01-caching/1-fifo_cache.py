#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that implements the First
      In First Out (FIFO) algorithm.
    When the number of items in the cache exceeds the limit,
      the first item put in cache is discarded.
    """

    def __init__(self):
        """Initialize the class and call the parent init"""
        super().__init__()
        self.order = []  # This will maintain the insertion order

    def put(self, key, item):
        """
        Add an item to the cache using the FIFO algorithm.
        If the cache exceeds its limit, the first item added will be removed.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        If the key doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
