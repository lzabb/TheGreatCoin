# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:58:06 2017

@author: Mas
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:49:46 2017

@author: Mas
"""



class blockchain(object):
    
   #moved the setting of a =  100 here as it should be a characteristic of the genkey funtion,
   #decoupled from the wallet object
  def genkey(self):
        total = np.random.randint(0,100,1)
        pubkey = np.random.randint(0,total,1)
        prikey = total-pubkey
        keys = [int(total),int(pubkey),int(prikey)]
        return keys
        
        
  def PoW(self, claimedprikey, bc, blockchain_DB, newowner_pk, howmuchbitcoins):
      
        def check(a, b):
            for item in a:
                if item[1] == b:
                    return item[0]
                else:
                    pass
            d = item[0]
            return d
            
        # New bitcoin created        
        bc1 = []
        for i in bc: 
            bc1.append(i)
        bc[0] = 10-howmuchbitcoins
        bc1[0] = howmuchbitcoins
        IDowner = bc1[-1] # pubkey=IDwallet
        
        # Check that newowner_pk is a valid pk (pk's are unique)
        flat_list_pk = []
        for w in blockchain_DB:
            flat_list_pk.append(w[1])
        if flat_list_pk.count(newowner_pk) == 1:
            
            # Check that claimedprikey is the correct prikey
            totalowner = check(blockchain_DB, IDowner)
            if claimedprikey+bc1[-1] == totalowner:
                bc1.append(newowner_pk)
                print 'Transaction accepted'
                coins = [bc, bc1] 
                return coins
                
            else:
                print ''' 
                Your transaction was rejected and unfortunately the reason cannot be disclosed. 
                A refund has been issued and should appear in your card statement within a few days. 
                We apologize for the inconvenience. 
                Actually you just gave us a wrong private key you little piece of mothermary...
                '''
                coins = [bc]
                return coins
                
        else:
            print 'Public key not valid'
            coins = [bc]
            return coins
     

      
class wallet(object):
  
    #the wallet is already initialized with its keys, as it makes more sense
    def __init__(self):
        self.keys = blockchain().genkey()
      
    def sign(self, guess, pubkey):
        if guess + pubkey  ==  total:
            answer = 'yes'
            return answer
        else :
            answer = 'no'
            return answer
    
    
    #BEGIN
import numpy as np


# Generating keys/wallets so that each key is unique
blockchain_DB = []
bc  =  [10]
w1 = wallet()
keys1 = w1.keys
blockchain_DB.append(keys1)
w2 = wallet()
keys2 = w2.keys
# Check of keys uniquness
keycheck = [keys1[0]-keys2[0],keys1[1]-keys2[1],keys1[2]-keys2[2]]
if keycheck.count(0) >= 1:
    print 'There was a collsion, new wallet regenerated'
    w2 = wallet()
    keys2 = w2.request_key(100)
else:
    pass
blockchain_DB.append(keys2)
print keys1, keys2
print blockchain_DB

# Begining of the transaction from Wallet 1 to Wallet 2
print 'Assign a bitcoin to Wallet 1'
bc.append(keys1[1])
print bc
print 'Transaction from Wallet 1 to Wallet 2'
IDowner= bc[-1]
print 'Input how much bitcoin you want to transfer? (Allowed (1,2,...,9,10))'
Howmuchbitcoins=raw_input(">")
howmuchbitcoins=int(Howmuchbitcoins)
print 'Input the publickey for the new owner' 
newowner_pk=raw_input(">")
newowner_pk=int(newowner_pk)
print 'Input the private key for'
print IDowner
Claimedprikey=raw_input(">")
claimedprikey=int(Claimedprikey)
b = blockchain()
coins = b.PoW(claimedprikey, bc, blockchain_DB, newowner_pk, howmuchbitcoins)
print 'Coins in the economy: [0] = amount, [-1] = pk_owner '
print coins
 



# SOME COMMENTS
# PoW: need a network and computations that check which bc belongs to who: some ideas: have all wallets denying to have received the bc
# Introduce hash method for chekcing right key
# clash same values in wallets
# TO DO: random wallet generation, cheking unique ID of wallets, create comunication between two wallets in transaction, proof-of-work (PoW)


























