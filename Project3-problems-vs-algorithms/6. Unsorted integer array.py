# -*- coding: utf-8 -*-
"""
Created on Tue May  4 00:10:03 2021

@author: User
"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """  
    
    # Double Traversal
    
    # Assume first element is minimum. Then, traverse to determine minimum
    minimum = ints[0]  
    arr = ints[1:]
    
    for current_ in arr:       
        
        if current_ < minimum:
            # maximum = minimum
            minimum = current_    
            
        
    # Assume first element is maximum. Then traverse to determine maximum
    maximum = ints[0]   
    arr = ints[1:]   
    
    for current_ in arr:         
        
        if current_ > maximum:
            # maximum = minimum
            maximum = current_      
            
            
    
    # Bonus: Single Traversal
    
    minimum = ints[0]   
    maximum = ints[0]
    arr = ints[1:]
    for current in arr:
        if current > maximum: 
            if maximum < minimum:
                minimum = maximum
            maximum = current     
            
        else: #current < maximum
            if current < minimum:     
                if minimum > maximum:
                    maximum = minimum
                minimum = current           

       
    return (minimum, maximum)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


l = [4, 1, 3, 6, 5, 0, 9 , 8, 2, 7]
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

# Edge (With negative numbers)
l = [i * -1 for i in l]
print ("Pass" if ((-9, 0) == get_min_max(l)) else "Fail")
# Pass

# Edge (With repeated numbers )
l = [1]*10
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
# Pass