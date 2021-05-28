# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:04:18 2021

@author: User
"""
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        print("Error! Input list cannot be empty")
        return 
    
    try:
        int(number)
    except:
        print("Error! Target number can only be an integer")
        return 
    
    start_index = 0
    last_index = len(input_list) - 1
    return rotated_array_helper(input_list, number, start_index, last_index)


def rotated_array_helper(array, target, start_index, last_index):
    mid_index = (start_index + last_index)//2
    
    if target == array[mid_index]:
        return mid_index
    
    if start_index > last_index:
        return -1 
    
    # If array to the left of target is sorted;
    if array[start_index] <= array[mid_index]:
        # Check for the key as we would a typical binary search.
        if array[start_index] <= target and target <= array[mid_index]:
            return rotated_array_helper(array, target, start_index, mid_index-1)
        
        else: # the target may be in the right array
            return rotated_array_helper(array, target, mid_index + 1, last_index)
        
    else: # if the array to the right is sorted;
        # Check for the key as we would a typical binary search.
        if array[mid_index] <= target and target <= array[last_index]:
            return rotated_array_helper(array, target, mid_index + 1, last_index)
        
        else: # the target may be in the left array
            return rotated_array_helper(array, target, start_index, mid_index - 1)
    

def linear_search(input_list, number):
    if len(input_list) == 0:        
        return
    if type(number) != int :
        return
    
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 10, 2, 3, 4], 10])
# Pass

# Edge Cases
test_function([[], 10])
# Error! Input list cannot be empty
# Pass

test_function([[6, 7, 8, 1, 2, 3, 4], ''])
# Error! Input list cannot be empty
# Pass
