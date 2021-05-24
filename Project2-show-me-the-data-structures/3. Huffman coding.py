# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:27:45 2021

@author: User
"""
import sys 

class Node():
    def __init__(self):
        self.value = None
        self.freq = None
        self.left_child = None
        self.right_child = None
        
    def set_value(self, value, freq):
        self.value = value
        self.freq = freq
        
    def get_value(self):
        return self.value, self.freq
        
    def set_left_child(self,value):
        self.left_child = value
        
    def set_right_child(self, value):
        self.right_child = value
        
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child != None
    
    def has_right_child(self):
        return self.right_child != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

   
class PriorityQueue(): 
    def __init__(self): 
        self.queue = [] 
        self.value_list = []
        self.freq_list = []
        self.num_elements = 0
  
    #def __str__(self): 
        #return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue) == 0
    
    def size(self):
        return self.num_elements
    
    def insert(self, node): 
        self.queue.append(node) 
        self.value_list.append(node.value)
        self.freq_list.append(node.freq)
        self.num_elements += 1
   
    def pop(self): 
        min_freq = min(self.freq_list)
        index = self.freq_list.index(min_freq)
        popped_node = self.queue[index]
        del self.queue[index]
        del self.freq_list[index]
        self.num_elements -= 1
        return popped_node
    
# Actual Encoding Starts Here..    

def huffman_encoding(raw_data):
    
    # PHASE 1: BUILD THE HUFFMAN TREE
    
    # Step 1 - First determine the frequency of each character in the data.
    my_data = {}
    for char in raw_data:
        my_data[char] = my_data.get(char, 0) + 1    
        
    # Step 2 - Create a priority queue with the dictionary    
    
    # First check for case where raw data is empty string 
    if raw_data == "":
        encoded_data = '0'     
        tree = Node()
        tree.value = raw_data
        return encoded_data, tree        
        
    # Now check for a case where the raw data is just one repeated letter.
    if len(my_data) == 1:
        encoded_data = '0'*my_data[char]     
        tree = Node()
        tree.value = list(my_data.keys())[0]
        tree.freq = my_data[char]
        return encoded_data, tree
    
    # Otherwise, continue with normal cases
    myQueue = PriorityQueue() 
    for key, val in my_data.items():
        this_node = Node()
        this_node.value = key
        this_node.freq = val
        myQueue.insert(this_node)
        

    # Step 3 to 8 - Pop-out two nodes with the minimum frequency from the priority queue and 
    # create a new node with a frequency equal to the sum of the two nodes picked  
    
    while myQueue.size() > 1:    
        # pop out two nodes with the least frequencies
        first_ele = myQueue.pop()
        second_ele = myQueue.pop()              
        
        # Create new node
        new_node = Node()
        new_node.value = None
        new_node.freq = first_ele.freq + second_ele.freq         
        new_node.set_left_child(first_ele)
        new_node.set_right_child(second_ele)
            
        # Add this new node to the priority queue
        myQueue.insert(new_node)           # Note that everytime insert is called, the queue size decreases by 1.
    
    
    # Store the root of the huffman tree
    huffman_tree = myQueue.queue[0]   
    

    #PHASE 2: GENERATE THE ENCODED DATA
    
    # Step 1: Traverse the tree and generate binary codes for the alphabet
    
    def tree_traverse_helper(huffman_tree):
        bin_codes = {}
        current_char_code = ""
        root = huffman_tree
        return tree_traverse(root, bin_codes, current_char_code)
          
    def tree_traverse(root, bin_codes, current_char_code):           
                
        if root is None:
            return 
        
        if root.left_child == None and root.right_child == None:
            bin_codes[root.value] = current_char_code    # stores the code for the character corresponding to
                                                         # root.value.
                       
        # traverse left and add "0" to the string
        tree_traverse(root.left_child, bin_codes, current_char_code + "0")
        
        # traverse right and add "1" to the string 
        tree_traverse(root.right_child, bin_codes, current_char_code + "1")
        
        return bin_codes
        
    
    huff_unique_characters_code = tree_traverse_helper(huffman_tree)    #Contains unique code for each character in the string
    
    # Step 2: Using the above character table to generate code for the string.
    encoded_data = ""
    for char in raw_data:
        encoded_data += huff_unique_characters_code.get(char,"")
    
    return encoded_data, huffman_tree
    

def huffman_decoding(coded_data, tree):   
    
    # Check for a scenario where the length of the coded data is just 1
    # i.e. the tree likely consists of only one character.    
    if len(coded_data) <= 1:
        return tree.value
    
    
    # Check for a case where the tree contains just one node
    if tree.left_child == None and tree.right_child == None:
        return tree.value * tree.freq
    
    
    # Now continue with the normal cases
    
    decoded_data = ""
    current_node = tree
    for bit in coded_data:
        if bit == '0':
            # travel left. shift node towards left
            current_node = current_node.left_child
        else:
            # travel right. shift node towards right
            current_node = current_node.right_child
            
        if (current_node.left_child == None) and (current_node.right_child ==  None):
            # This is a leaf node
            decoded_data += current_node.value
            # restore tree
            current_node = tree
    
    return decoded_data



def testing_function(data):
        
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
# Test Case 1
testing_function("AAAAAAABBBCCCCCCCDDEEEEEE")
# The size of the data is: 74
# The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE
# The size of the encoded data is: 32
# The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101
# The size of the decoded data is: 74
# The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE
   
# Test Case 2
testing_function("The bird is the word")
# The size of the data is: 69
# The content of the data is: The bird is the word
# The size of the encoded data is: 36
# The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010
# The size of the decoded data is: 69
# The content of the encoded data is: The bird is the word


# Test Case 3 (Extreme Case: where all characters have frequency of 1)
testing_function("ABCDEF")
# The size of the data is: 55
# The content of the data is: ABCDEF
# The size of the encoded data is: 28
# The content of the encoded data is: 1001011101110001
# The size of the decoded data is: 55
# The content of the encoded data is: ABCDEF

# Test Case 4 (Edge Case: where only one character is repeated)
testing_function("AAAAAA")
# The size of the data is: 55
# The content of the data is: AAAAAA
# The size of the encoded data is: 24
# The content of the encoded data is: 000000
# The size of the decoded data is: 55
# The content of the encoded data is: AAAAAA


# Test Case 5 (Edge Case: where the data is empty string)
testing_function("")
# The size of the data is: 51
# The content of the data is: 
# The size of the encoded data is: 24
# The content of the encoded data is: 0
# The size of the decoded data is: 51
# The content of the encoded data is: 
    
         