#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that implements
      the Most Recently Used (MRU) algorithm.
      When the number of items in the cache exceeds MAX_ITEMS,
      the most recently used item is discarded.
    """

    def __init__(self):
        """Initialize the class and call the parent init"""
        super().__init__()
        self.mru_key = None  # Track the most recently used key

    def put(self, key, item):
        """
        Add an item to the cache using the MRU algorithm.
        If the cache exceeds its limit, the most recently used item is removed.
        """
        if key is None or item is None:
            return

        if len(self.cache_data
               ) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            if self.mru_key:
                print(f"DISCARD: {self.mru_key}")
                del self.cache_data[self.mru_key]

        # Add or update the cache
        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """
        Retrieve an item from the cache using the MRU algorithm.
        If the key is None or doesn't exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_key = key  # Mark this key as most recently used
        return self.cache_data.get(key)
