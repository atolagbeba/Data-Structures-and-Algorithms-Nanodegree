# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:38:12 2021

@author: User
"""
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler
        

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for partOfpath in path:
            current_node.insert(partOfpath)
            current_node = current_node.children[partOfpath]
            
        current_node.handler = handler
        

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        current_node = self.root
        for partOfpath in path:
            if partOfpath in current_node.children:
                current_node = current_node.children[partOfpath]
            else:
                return None
            
        return current_node.handler
        

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, partOfpath):
        # Insert the node as before
        if partOfpath not in self.children:            
            self.children[partOfpath] = RouteTrieNode()
    

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(handler)


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        
        path = self.split_path(path)
        self.router.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler 
        
        path = self.split_path(path)
        
        if len(path) == 0:
            return self.router.handler
        
        if self.router.find(path) is not None:
            return self.router.find(path)
        
        else:
            return "None"
        

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        
        parts = path.split(sep = '/')
        partsList = [i for i in parts if i != ""]
        
        return partsList

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
# root handler
print(router.lookup("/home")) # (Edge case) should print 'not found handler' or None if you did not implement one
# None
print(router.lookup("/home/about")) # should print 'about handler'
# about handler
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
# about handler
print(router.lookup("/home/about/me")) # (Edge case) should print 'not found handler' or None if you did not implement one
# None