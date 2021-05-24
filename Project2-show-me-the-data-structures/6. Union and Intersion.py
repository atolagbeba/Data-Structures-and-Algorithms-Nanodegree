# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:41:03 2021

@author: User
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    check_list = []
    myLinkedList = LinkedList()   #Empty linkedlist to store union elements
    
    # first iterate over the first linkedlist
    
    node = llist_1.head
    while node:
        if node.value not in check_list:
            myLinkedList.append(node.value)
            check_list.append(node.value)
            
        node = node.next    
           
    # then iterate over the second linked list.
    node = llist_2.head
    while node:
        if node.value not in check_list:
            myLinkedList.append(node.value)
            check_list.append(node.value)
            
        node = node.next 
        
        
    if myLinkedList.head == None:
        return None
    
    return myLinkedList

        
def intersection(llist_1, llist_2):
    # Your Solution Here
    check_list_1 = []
    check_list_2 = []
    myLinkedList = LinkedList()   #Empty linkedlist to store common elements
        
   # first iterate over the first linkedlist
    
    node = llist_1.head
    while node:
        if node.value not in check_list_1:            
            check_list_1.append(node.value)
            
        node = node.next    
           
    # then iterate over the second linked list.
    node = llist_2.head
    while node:
        if node.value in check_list_1 and node.value not in check_list_2:
            myLinkedList.append(node.value)
            check_list_2.append(node.value)
            
        node = node.next 
    
    if myLinkedList.head == None:
        return None
    
    return myLinkedList

        

def test_function(element_1, element_2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)


    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

# Test case 1
print('\nTest case 1:\n')

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]


test_function(element_1, element_2)

# Expected Output: 
  # Union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
  # Intersection: 6 -> 4 -> 21 ->   


# Test case 2
print('\nTest case 2:\n')

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

test_function(element_1, element_2)
# Expected Output: 
  # Union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
  # Intersection: None

# Test case 3 (Edge Case)
print('\nTest case 3:\n')

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

test_function(element_1, element_2)
# Expected Output: 
  # Union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 ->  
  # Intersection: None


# Test case 4 (Edge Case)
print('\nTest case 4:\n')

element_1 = []
element_2 = []

test_function(element_1, element_2)
# Expected Output: 
  # Union: None
  # Intersection: None