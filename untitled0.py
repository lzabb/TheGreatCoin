# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:07:50 2017

@author: zabbanl
"""
#4TO DO: bc splitting, random wallet generation, cheking unique ID of wallets, create comunication between two wallets in transaction, proof-of-work (PoW)
class blockchain(object):
   
    
    def genkey(self, a):
        total = np.random.randint(0,a,1)
        pubkey = np.random.randint(0,total,1)
        prikey = total-pubkey
        keys = [int(total), int(pubkey), int(prikey)]
        return keys
   
        
    def PoW(self, claimedprikey, bc, blockchain_DB, newownerpubkey):
         
        def check(a, b):
            for item in a:
                if item[1] == b:
                    return item[0]
                else:
                    pass
            d = item[0]
            return d        
        
        IDowner = bc[-1] #pubkey=IDwallet
        totalowner = check(blockchain_DB, IDowner)
        
        if claimedprikey + IDowner == totalowner:
            bc.append(newownerpubkey)
            print 'Transaction accepted'
            return bc
        else:
            print 'Your transaction was rejected and unfortunately the reason cannot be disclosed. A refund has been issued and should appear in your card statement within a few days. We apologize for the inconvenience.'
            return bc
            
  
            
class wallet(object):
    
    
    def request_key(self, a):
        b = blockchain()
        keys = b.genkey(a)
        return keys
  
        
    def sign(self, guess, pubkey):
        if guess+pubkey  ==  total:
            answer = 'yes'
            return answer
        else:
            answer = 'no'
            return answer
     
     
    #BEGIN
 
import numpy as np


blockchain_DB = []
bc  =  []
w1 = wallet()
keys1 = w1.request_key(100)
blockchain_DB.append(keys1)
w2 = wallet()
keys2 = w2.request_key(100)
blockchain_DB.append(keys2)
print keys1, keys2
print blockchain_DB
print 'Assign a bitcoin to Wallet 1'
bc.append(keys1[1])
print bc
print 'Transaction from Wallet 1 to Wallet 2'
IDowner= bc[-1]
print 'Input the publickey for the new owner'
Newownerpubkey=raw_input(">")
newownerpubkey=int(Newownerpubkey)
print 'Input the private key for'
print IDowner
Claimedprikey=raw_input(">")
claimedprikey=int(Claimedprikey)
b = blockchain()
b.PoW(claimedprikey, bc, blockchain_DB, newownerpubkey)
 