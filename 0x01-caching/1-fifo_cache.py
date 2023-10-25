#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import deque
from typing import Any, Dict, Optional


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - Caching system inherit from BaseCaching
    """

    def __init__(self):
        """ Instantiation
        """
        super().__init__()
        self.queue = deque()

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache using the FIFO mode.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.queue.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.queue.popleft()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
