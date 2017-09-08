"""
Custom implementation of hashtable.
"""

from __future__ import print_function


########## hashtable class
class hashtable(object):
    """
    hashtable stores data as a list of <key,value> pairs. 
    key is a string, val is any object that stores data.
    """
    def __init__(self, capacity=200):        
        self._capacity = capacity
        self._size = 0
        self._data = [None]*self._capacity
        self._keys = [[None] for _ in range(capacity)]]

    def set_value(key): 
   	
