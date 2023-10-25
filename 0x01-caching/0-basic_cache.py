#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from typing import Any, Dict, Optional


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - caching system inherit from BaseCaching
    """

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
