#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching
from collections import deque
from typing import Any, Dict, Optional


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - caching system inherit from BaseCaching
    """

    def __init__(self):
        """ Instantiation
        """
        super().__init__()
        self.queue = deque()

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache using LIFO algorithm.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
