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
        """ Add an item in the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_freq = min(self.frequency.values())
                    min_keys = [
                        k for k, v in self.frequency.items() if v == min_freq
                    ]
                    discard_key = min_keys[0]

                    if len(min_keys) == 1:
                        del self.cache_data[discard_key]
                        del self.frequency[discard_key]
                    else:
                        for k in self.order:
                            if k in min_keys:
                                del self.cache_data[k]
                                del self.frequency[k]
                                break

                    print("DISCARD: {}".format(discard_key))

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.order[key] = None

    def get(self, key: Any) -> Optional[Dict[Any, Any]]:
        """ Get an item by key.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.order.move_to_end(key)
            return self.cache_data[key]

        return None
