# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:42:30 2021

@author: User
"""
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
      
    """
    if not os.path.isdir(path):
        return "Invalid path"

    output_list = []
    return find_files_helper(output_list,suffix, path) 
    
       
def find_files_helper(output_list, suffix, path):
    helper_list = []
    if len(os.listdir(path)) == 0:
        return []
    
    else:
        for sub_path in os.listdir(path):
            if '.' in sub_path:   #This is a file 
                if sub_path.endswith(suffix):
                    helper_list.append(sub_path)
            else:                 # This is a folder
                sub_path = os.path.join(path, sub_path)
                find_files_helper(output_list,suffix, sub_path)
                
        output_list.extend(helper_list)

    return output_list
        
        
# Test Case 1
suffix = ".c"
path = os.getcwd()
print(find_files(suffix, path))
# ['a.c', 'b.c', 'a.c', 't1.c']


# Test Case 2
suffix = ".h"
path = os.getcwd()
print(find_files(suffix, path))
# ['a.h', 'b.h', 'a.h', 't1.h']

# Test Case 3
suffix = ".x"
path = os.getcwd()
print(find_files(suffix, path))
# []

# Test Case 4 (Edge Case with blank suffix)
suffix = " "
path = os.getcwd()
print(find_files(suffix, path))
# []


# Test Case 4 (Edge Case with invalid path)
path = " "
print(find_files(suffix, path))
# Invalid path
