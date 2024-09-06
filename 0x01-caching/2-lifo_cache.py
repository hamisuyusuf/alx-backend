#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that follows 
    the Last-In First-Out (LIFO) algorithm.
    If the number of items exceeds BaseCaching.MAX_ITEMS,
      the last item added will be discarded.
    """

    def __init__(self):
        """Initialize the class and call the parent init"""
        super().__init__()
        self.last_key = None  # Keep track of the most recent key

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO algorithm.
        If the cache exceeds its limit, the last item added will be removed.
        """
        if key is None or item is None:
            return

        # If the cache is full, discard the last added key (LIFO)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        # Add the new key-value pair
        self.cache_data[key] = item
        self.last_key = key  # Update the last added key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        If the key doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
