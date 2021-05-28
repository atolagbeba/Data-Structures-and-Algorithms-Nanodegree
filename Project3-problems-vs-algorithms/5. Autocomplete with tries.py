# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:57:52 2021

@author: User
"""
            
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
              
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:            
            self.children[char] = TrieNode()
            
    def suffixes(self, suffix = ''):          
        
        # First check for edge case where the root is empty:
        if self is None:
            return "Trie is empty"
         
        outputList = []
        
        if self.children == {}:
            return outputList       
               
        current_node = self.children
        
        for char in current_node:
            suffix = suffix + char
            if current_node[char].is_word:
                outputList.append(suffix)            
            
            outputList.extend(current_node[char].suffixes(suffix))         
            
            # We are done with this char, restore suffix to a state before adding char
            suffix = suffix[0:-1]
        return outputList

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:      
            current_node.insert(char)  
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        # First check for edge case where the root is empty        
        if self.root.children == {}:
            return TrieNode()
        
        # Now continue with normal case where root is not empty        
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
            
        return current_node
      
    
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
prefixNode = MyTrie.find('ant')
print(prefixNode.suffixes())    
# ['hology', 'agonist', 'onym']

prefixNode = MyTrie.find('tr')
print(prefixNode.suffixes())     
# ['ie', 'igger', 'igonometry', 'ipod']

# Edge Case (Null prefix)
prefixNode = MyTrie.find('')
print(prefixNode.suffixes())   
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 
# 'trigonometry', 'tripod']


# Edge Case (Empty trie)
MyTrie = Trie()    
prefixNode = MyTrie.find('an')
print(prefixNode.suffixes())
# []



