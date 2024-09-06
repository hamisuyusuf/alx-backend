#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that implements the Least Recently Used (LRU) algorithm.
    When the number of items in the cache exceeds MAX_ITEMS, the least recently used item is discarded.
    """

    def __init__(self):
        """Initialize the class and call the parent init"""
        super().__init__()
        self.lru_order = []  # This will maintain the order of use of cache items

    def put(self, key, item):
        """
        Add an item to the cache using the LRU algorithm.
        If the cache exceeds its limit, the least recently used item is removed.
        """
        if key is None or item is None:
            return

        # If key already exists, update its value and mark it as recently used
        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add or update the cache
        self.cache_data[key] = item
        self.lru_order.append(key)  # Mark as recently used

    def get(self, key):
        """
        Retrieve an item from the cache using the LRU algorithm.
        If the key is None or doesn't exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data.get(key)
