# alx-backend

## 0x01. Python - Caching

This repo is for learning about caching systems and how to implement them in Python.

### Description of what each file shows:

* main_files ----- Folder holding main programs to showcase examples of how to use functions
0. basic_cache.py - Basic dictionary caching system with expiration time for stored keys
1. fifo_cache.py - Dictionary caching system with expiration time for stored keys and first in first out system
2. lru_cache.py - Dictionary caching system with expiration time for stored keys and least recently used system
3. mru_cache.py - Dictionary caching system with expiration time for stored keys and most recently used system
4. lfu_cache.py - Dictionary caching system with expiration time for stored keys and least frequently used system
5. mruru_cache.py - Dictionary caching system with expiration time for stored keys and most recently used and recently used system
6. basic_caching.py - Basic dictionary caching system with expiration time for stored keys

### Environment

* Language: Python 3.4.3
* OS: Ubuntu 14.04 LTS
* Compiler: python3
* Style guidelines: PEP 8 (version 1.7) for Python 3.5
* Module version: 0x01. Caching systems

## Resources

* [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
* [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
* [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
* [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
* [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Learning Objectives

* **Caching System**: A high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than accessing the data’s primary storage location.
* **FIFO**: "First-In, First-Out", an asset-management and valuation method where the assets produced or acquired first are sold, used, or disposed of first.
* **LIFO**: "Last-In, First-Out", an accounting method where the assets purchased or acquired last are disposed of first.
* **LRU**: "Least Recently Used", a type of cache algorithm used to manage memory within a computer.
* **MRU**: "Most Recently Used", often used in reference to the files on your computer that you've accessed most recently.
* **LFU**: "Least Frequently Used", a cache algorithm that optimizes computer memory by tracking how many times a block is referred in memory.
* **Purpose of a Caching System**: To improve the performance and efficiency of a system by reducing the amount of time it takes to access frequently accessed data.
* **Limits of a Caching System**: Can introduce issues with data consistency, particularly in systems where multiple users or applications are accessing the same data.

