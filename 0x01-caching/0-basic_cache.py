#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple caching system that inherits from BaseCaching.
    There is no limit to the cache size.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        If key is None or the key doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
