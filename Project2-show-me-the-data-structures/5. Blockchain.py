# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:16:19 2021

@author: User
"""
import time
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)  
        self.next = None
        
    
    def __repr__(self):
        return ' Data: {} \n Timestamp: {} \n Hash: {} \n'.format(self.data, self.timestamp, self.hash)
    
    
    def calc_hash(self, data):
        # Determines the sha256 hash corresponding to a given string.
        
        sha = hashlib.sha256()
        
        hash_str = data.encode('utf-8')

        sha.update(hash_str)
        
        # return the calculated hash
        return sha.hexdigest()
    

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_block = 0
        
    
    def append(self, data):
        
        timestamp = time.time()
               
        if self.head is None:            
            previous_hash = None
            self.head = Block(timestamp, data, previous_hash)
            self.tail = self.head
           
            
        else:
            previous_hash = self.tail
            self.tail.next = Block(timestamp, data, previous_hash)
            self.tail  = self.tail.next
            
            
        self.num_block += 1 
                   

    def size(self):
        return self.num_block
    
    
    def _print_(self):
        current_block = self.head
        for _ in range(self.size()):
            print(current_block)
            current_block = current_block.next
            
    
#Testing

# Normal Case when the timestamps vary
my_blockchain = BlockChain()

# Append the blocks and add time delays to vary the timestamp

# Test case 1
my_blockchain.append('Tunde Comes from Africa')
time.sleep(3) # Sleep for 3 seconds

# Test Case 2
my_blockchain.append('Murad Comes from Bangladesh')
time.sleep(3) # Sleep for 3 seconds

# Test case 3
my_blockchain.append('Maxwell Comes from Kenya')
time.sleep(3)

# Let's see the blocks in the BlockChain
my_blockchain._print_()



# Edge Case: With same time stamp

# Don't add delay to next ones to see the effect of same timestamps (Edge Cases)

my_blockchain = BlockChain()
# Test cases 4-6
my_blockchain.append('Kelvin Comes from Tanzania')
my_blockchain.append('Alex comes from USA')
my_blockchain.append('Salah comes from Egypt')

# Test case 5 (Edge with empty string)
# What if the data is an empty string
my_blockchain.append("")


# Print the bloacks in the blockchain
my_blockchain._print_()
# Data: Tunde Comes from Africa 
# Timestamp: 1612672534.088037 
# Hash: dd646ce1432990f9ef1d33b36e7e2e419f9a29630e686e314683354d2fa76178 

# Data: Murad Comes from Bangladesh 
# Timestamp: 1612672534.0890353 
# Hash: 4dc2b2ba6b6ee37b42077a98fe688ea9d4d74c7000004287f562de801191d56d 

# Data: Maxwell Comes from Kenya 
# Timestamp: 1612672534.0890353 
# Hash: f61e2b208c2382a7a0c7b06310faccb0024170398d6b78fe4b6cc1a340b4881c 

# Data: Kelvin Comes from Tanzania 
# Timestamp: 1612672534.0890353 
# Hash: 2d83a7a33442c4dba6580e33df086fa2536b3905940c1933230381e39ca51f97 

# Data: Alex comes from USA 
# Timestamp: 1619885402.6300426 
# Hash: 61a17a79445fb2c16e8de067be2d20950eaf43c7511bfea40006e9a547492d3f

# Data: Salah comes from Egypt 
# Timestamp: 1619886155.508953 
# Hash: 775528da5227d7c99db785ed74349e908d66e02a7872d73d64d7e5b7c359c62a 

# Data:  
# Timestamp: 1619878139.7471764 
# Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 
