#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict
from typing import Any, Dict, Optional


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - Caching system inherit from BaseCaching
    """

    def __init__(self):
        """ Instantiation
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.move_to_end(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = next(reversed(self.order.items()))
                del self.cache_data[discard_key]
                del self.order[discard_key]
                print("DISCARD: {}".format(discard_key))

            self.order[key] = None
            self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key.
        """
        if key is not None and key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]

        return None
