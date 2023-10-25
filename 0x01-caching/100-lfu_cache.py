#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict
from typing import Any, Dict, Optional


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Caching system inherit from BaseCaching
    """

    def __init__(self):
        """ Instantiation
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            pass

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key.
        """
        if key is not None and key in self.cache_data:
            pass
        return None
