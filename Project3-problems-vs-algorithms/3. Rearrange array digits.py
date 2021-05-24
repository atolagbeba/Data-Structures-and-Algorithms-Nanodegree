# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:40:19 2021

@author: User
"""
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # To accommodate for edge case with negative integers:
    input_list = [-1*i if i<0 else i for i in input_list]    
    
    # First sort the list using Merge Sort
    startIndex = 0
    lastIndex = len(input_list) - 1
    mergedList = mergeSort(input_list, startIndex, lastIndex)
    
    # Then generate two lists that would yield maximum sum when the integer
    # formed by the order of the elements are added.
    
    # To accommodate for edge case with negative integers:
    
    arr1 = mergedList[-1::-2]
    arr2 = mergedList[-2::-2]
    
    # Convert the two resulting lists to numbers
    number1 = int("".join((map(str, arr1))))
    number2 = int("".join((map(str, arr2))))
    
    # return a list of these numbers
    return [number1, number2]


def mergeSort(input_list, startIndex, lastIndex):
    
    if startIndex >= lastIndex:
        return input_list[startIndex:lastIndex+1]
    
    midIndex = (startIndex + lastIndex) // 2
    
    # Divide the array into two parts recursively
    arr_left = mergeSort(input_list, startIndex, midIndex)
    arr_right = mergeSort(input_list, midIndex+1, lastIndex)
    
    mergedList = merge(arr_left, arr_right)    
    
    return mergedList

def merge(arr_left, arr_right):
    # Assuming both arr_left and arr_right are sorted
    
    outputList = []
    
    # while both lists are non empty;
    while len(arr_left) >= 1 and len(arr_right) >= 1:
        # Compare first elements of both arr_left and array_2
        # Sorting is being done in reverse.
        i = arr_left[0]
        j = arr_right[0]
        
        if i <= j:
            outputList.append(i)
            arr_left.pop(0)
        else:
            outputList.append(j) 
            arr_right.pop(0)
    
    # Check if there are still elements in arr_left          
    if len(arr_left) >= 1:
        outputList.extend(arr_left)

    # Check if there are still elements in arr_right. 
    if len(arr_right) >= 1:
        outputList.extend(arr_right)
        
    return outputList
            


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Normal Case
test_function([[1, 2, 3, 4, 5], [542, 31]])    
# Pass

# Normal Case
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass

# Edge Case (Negative Integers)
test_function([[4, -6, 2, 5, -9, 8], [964, 852]])
# Pass

# Edge Case (Large array)
test_function([[i for i in range(0, 100)], [99979593918987858381797775737169676563615957555351494745434139373533312927252321191715131197531, 98969492908886848280787674727068666462605856545250484644424038363432302826242220181614121086420]])
# Pass
