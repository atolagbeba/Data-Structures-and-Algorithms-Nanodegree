# -*- coding: utf-8 -*-
"""
Created on Sat May 22 01:32:47 2021

@author: User
"""

import math
import heapq

class GraphNode():
    def __init__(self, iD, coordinate):
        self.id = iD
        self.coordinate = coordinate
        self.children = []
        self.g = 0               # actual distance from start node
        self.h = math.inf        # estimated (heurestic) distance to end node
        self.f = math.inf
        self.parent = None       # Helps keep track of the immediate node traveresed to reach this node.
        
    def add_child(self, newNode):
        self.children.append(newNode)
        
    def remove_child(self, delNode):
        self.children.remove(delNode)
        
        
class Graph():
    def __init__(self, nodes_list):
        self.nodes = nodes_list
        
    def add_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)
            
            
        
def getDistance(node1, node2):
    """ 
    Function estimates the ecluidean distance between two nodes.
    Inputs are two nodes whose distance apart is to be determined.
    Output is an integer value representing the distance between the two nodes.
    """
    x1, y1 = node1.coordinate
    x2, y2 = node2.coordinate
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return distance


def shortest_path(M, start, goal):       
    
    # Generate nodes_list from given dictionary.
    nodes_list = [] 
    for iD, coordinate in M.intersections.items():
        newNode = GraphNode(iD, coordinate)
        newNode.iD = iD
        newNode.coordinate = coordinate
        nodes_list.append(newNode)
    

    # Initialize the graph.
    myGraph = Graph(nodes_list)

    # Link the nodes in the graph by adding edges (i.e connectivities)
    # No edge weights are assumed here.

    for index, connectivity in enumerate(M.roads):
        node1 = nodes_list[index]   # parent node
    
        for i in connectivity:      # get each child node
            node2 = nodes_list[i]
        
            # link node 1 and node 2
            myGraph.add_edge(node1, node2)
        
        
        
    # Now that the graph is fully ready, we can start traversing

    openedNodes = []  # List to keep track of nodes being explored.
    closedNodes = []  # List to keep track of explored nodes. 
                      # A node is marked explored when all its children has been visited.

    # Start from the start node and set its value for g as zero (i.e. node.g = 0).
    # Also, detertmine its h value (i.e. node.h) using ecluidean distance
    current_node = nodes_list[start]
    current_node.g = 0
    current_node.h = getDistance(current_node, nodes_list[goal])

    while current_node.iD != goal:
        # get the children and apend to openedNodes.
        for child in current_node.children:
            if child not in openedNodes and child not in closedNodes:   
                openedNodes.append(child)
                child.g = current_node.g + getDistance(current_node, child)
                child.h = getDistance(child, nodes_list[goal])
                existing_f = child.f
                new_f = child.g + child.h              
                
                if new_f < existing_f:   # Otherwise, do nothing.
                    child.f = new_f
                    
                    # Set this child's parent node as the current_node
                    # This will help us track the path taken to reach the child.
                    child.parent = current_node
                    
        # At the end of the for loop, all the children of current_node has been explored.
        # Therefore, we update the closedNodes list to reflect this.
        closedNodes.append(current_node)
        
        # Of all opened nodes, we determine the one with minimum f value, we remove that node from openedNodes list and
        # continue the next step from that node by setting it as current_node.
        
        hp = []
        for node in openedNodes:
            heapq.heappush(hp, (node.f, node))
            
        minNode = heapq.heappop(hp)
        
        openedNodes.remove(minNode[1])
        
        current_node = minNode[1]
        
    
    # Having traversed the nodes from start to goal, we determine the path taken to goal.
    PathTakenReversed= [goal]
    
    current_node = nodes_list[goal]   
    
    while current_node.parent != None:
        PathTakenReversed.append(current_node.parent.iD)
        current_node = current_node.parent
    
    PathTaken = []
    for node in reversed(PathTakenReversed):
        PathTaken.append(node)
    
    PathTaken = PathTakenReversed[::-1]  
       
    return PathTaken