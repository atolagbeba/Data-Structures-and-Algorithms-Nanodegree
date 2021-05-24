# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:51:33 2021

@author: User
"""
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """        
    if number < 0:
        return "Enter a positive number"
    
    if number == 0 or number == 1:
        return number
        
    return sqrt_helper(number, 0, number)


def sqrt_helper(number, lower_limit, upper_limit):
    half_number = (lower_limit + upper_limit) / 2
    
    if (half_number ** 2) == number:
        return int(half_number)
    
    if abs(number - (half_number **2)) <= 1:
        return int(half_number)
    
    elif (half_number ** 2) < number:
        return sqrt_helper(number, half_number, upper_limit)
    
    else:    # (half_number ** 2) > number:        
        return sqrt_helper(number, lower_limit, half_number)
    

# Sample test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


print("\nEdge Cases:\n")

# Edge Case
print(sqrt(-1))
# Enter a positive number

# Edge Case 
print(sqrt(0))
# 0

# very large test case 
print(sqrt(100000))
# 316