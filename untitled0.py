# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:49:06 2017

@author: Mas
"""

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
    
   
    def __init__(self):
        self.blockchain_keys = []
        self.bc  =  [10]
    
    #moved the setting of a =  100 here as it should be a characteristic of the genkey funtion,
   #decoupled from the wallet object
    def genkey(self, blockchain_keys, fn):
        total = np.random.randint(1,10000,1) 
        pubkey = np.random.randint(0,total,1)
        prikey = total-pubkey
        keys = {'total': int(total), 'pubkey': int(pubkey), 'prikey': int(prikey)}
        if blockchain_keys == []:
            blockchain_keys.append(keys)
            return keys
        else:
            answer_from = fn(keys)
            while answer_from == 'collision':
                print 'Collision: new key generated'
                total = np.random.randint(1,10000,1) 
                pubkey = np.random.randint(0,total,1)
                prikey = total-pubkey
                keys = {'total': int(total), 'pubkey': int(pubkey), 'prikey': int(prikey)}
                answer_from = fn(keys)
                if answer_from != 'collision':
                    break
            return answer_from[-1]
            
        
    def PoW(self, claimedprikey, bc, blockchain_keys, newowner_pk, howmuchbitcoins):
        if bc[0] < howmuchbitcoins:
            print 'Insufficient funds'
        else:
            def check(a, b):
                for item in a:
                    if item['pubkey'] == b:
                        return item['total']
                    else:
                        pass
                d = item['total']
                return d
                
            # New bitcoin created        
            bc1 = list(bc)
            bc1[0] = howmuchbitcoins
            IDowner = bc1[-1] # pubkey=IDwallet
            
            # Check that newowner_pk is a valid pk (pk's are unique)
            flat_list_pk = []
            for w in blockchain_keys:
                flat_list_pk.append(w['pubkey'])
            if flat_list_pk.count(newowner_pk) == 1:
                
                # Check that claimedprikey is the correct prikey
                totalowner = check(blockchain_keys, IDowner)
                if claimedprikey+bc1[-1] == totalowner:
                    bc1.append(newowner_pk)
                    bc[0] = 10-howmuchbitcoins
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
    # Generating keys/wallets so that each key is unique
    # the wallet is already initialized with its keys, as it makes more sense
    def __init__(self):
        self.keys = blockchain().genkey(blockchain_keys, database_enquiry)





# Module
def database_enquiry(keys_new):
        keycheck = []
        for k in blockchain_keys:
            keycheck.append(k['total']-keys_new['total'])
            keycheck.append(k['pubkey']-keys_new['pubkey'])
            keycheck.append(k['prikey']-keys_new['prikey'])
        if keycheck.count(0) >= 1:
            return 'collision'
        else:
            blockchain_keys.append(keys_new)
            return blockchain_keys
            print keys_new
            

    
    #BEGIN
import numpy as np


b = blockchain()
blockchain_keys = b.blockchain_keys
bc = b.bc

print 'Input how many wallets you want in the economy (do not choose more than 500)' 
number_of_wallets = raw_input(">")
number_of_wallets = int(number_of_wallets)
steps = np.arange(number_of_wallets)
for steps in steps:
    w = wallet()
    keys = w.keys
    print keys
    
print blockchain_keys

# Begining of the transaction from Wallet 1 to Wallet 2
print 'Assign a bitcoin to Wallet 1'
bc.append(blockchain_keys[0]['pubkey'])
print bc
print 'Transaction from Wallet 1 to another Wallet'
IDowner= bc[-1]
print 'Input how much bitcoin you want to transfer? (Allowed (1,2,...,9,10))'
Howmuchbitcoins = raw_input(">")
howmuchbitcoins = int(Howmuchbitcoins)
print 'Input the publickey for the new owner' 
newowner_pk = raw_input(">")
newowner_pk = int(newowner_pk)
print 'Input the private key for'
print IDowner
Claimedprikey = raw_input(">")
claimedprikey = int(Claimedprikey)
coins = b.PoW(claimedprikey, bc, blockchain_keys, newowner_pk, howmuchbitcoins)
print 'Coins in the economy: [0] = amount, [-1] = pk_owner '
print coins
 



# SOME COMMENTS
# Track wallets balance
# PoW: need a network and computations that check which bc belongs to who: some ideas: have all wallets denying to have received the bc
# Introduce hash method for chekcing right key
# clash same values in wallets
# TO DO: random wallet generation, cheking unique ID of wallets, create comunication between two wallets in transaction, proof-of-work (PoW)
# coin























