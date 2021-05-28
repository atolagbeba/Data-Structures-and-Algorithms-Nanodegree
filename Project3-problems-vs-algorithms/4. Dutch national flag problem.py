# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:14:12 2021

@author: User
"""
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # First count the number of Os, 1s, and 2s in the array.
    
    if len(input_list) == 0:
        return "Error! Input list cannot be empty"
    
    count ={}     
    for k in input_list:
        if k < 0 or k > 2:
            return "Error! Input list can only contain one of 0, 1 and 2."
        count[k] = count.get(k,0) + 1
        
     # Now multiply the counts for each digit in te list by the counts.     
    zeros_list = [0] * count[0]
    ones_list = [1] * count[1]
    twos_list = [2] * count[2]
     
    output_list = zeros_list + ones_list + twos_list
        
    return output_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)


# Test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

# Edge cases
test_function([])
# Error! Input list cannot be empty

# Edge case
test_function([0, 1, 2, 3, 0, 2, 1, 0])
# Error! Input list can only contain one of 0, 1 and 2.
