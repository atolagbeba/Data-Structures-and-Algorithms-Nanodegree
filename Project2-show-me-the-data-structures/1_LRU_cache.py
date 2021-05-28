# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:05:21 2021

@author: User
"""
from collections import OrderedDict

class LRU_Cache(object):   
    
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity        
        self.visited_keys = OrderedDict()        
        return

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
                
        if key in self.visited_keys: 
            value = self.visited_keys[key]
                        
            # Mark this key as a recently visited by restoring its order in an ordered dictionary. 
            # This is achieved by first deleting it and then re-adding it to the end of the dictionary.
            del self.visited_keys[key]
            self.visited_keys[key] = value
                       
            # Then return the value of the key.        
            print(value)
            return value              # Cache hit!
        
        # otherwise return -1
        print(-1)        
        return -1          # Cache miss!
        

    def set(self, key, value):
        if type(self.capacity) != int:
            print('Capacity is invalid')
            return 
        
        if self.capacity < 1:
            print('Capacity is negative')
            return 
        
        # Update the visited_keys dictionary if key already exists.        
        if key in self.visited_keys:
            # Although key already exists, it has just been queried i.e. meaning it is being visited.
            # So, mark this key as a recently visited by restoring its order in an ordered dictionary. 
            # This is achieved by first deleting it and then re-adding it to the end of the dictionary.
            
            del self.visited_keys[key]
            self.visited_keys[key] = value           
        
        # Otherwise, set the value if the key is not present in the cache.             
        if key not in self.visited_keys:
            # Check if the cache is at full capacity and remove the oldest item.
            
            if len(self.visited_keys) < self.capacity:                
                self.visited_keys[key] = value               
                
            else: 
                # Remove the oldest / least used item and remove it  i.e. the first
                # element of the OrderedDict
                self.visited_keys.popitem(0)
                
                # Then insert the new key-value pair into the dictionary               
                self.visited_keys[key] = value                
    
        return 
        
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


# Test Case 1
our_cache.get(1)       
# returns 1

# Test Case 2
our_cache.get(2)       
# returns 2 

# Test Case 3
our_cache.get(9)      
# returns -1 

our_cache.set(5, 5) 
our_cache.set(6, 6)

# Test Case 4
our_cache.get(3)      
# returns -1 

# Edge Case
our_cache.get(" ")  
# returns -1

# Edge Case
our_cache = LRU_Cache(" ")
our_cache.set(1, 1);
# returns Capacity is invalid

# Edege Case
our_cache = LRU_Cache(-1)
our_cache.set(1, 1);
# returns Capacity is  negative
