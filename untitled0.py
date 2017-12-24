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
        self.coin = []
    
    #moved the setting of a =  100 here as it should be a characteristic of the genkey funtion,
   #decoupled from the wallet object
    def genkey(self):
        total = np.random.randint(1,10000,1) 
        pubkey = np.random.randint(0,total,1)
        prikey = total-pubkey
        keys = {'total': int(total), 'pubkey': int(pubkey), 'prikey': int(prikey)}
        if blockchain_keys == []:
            blockchain_keys.append(keys)
            return keys
        else:
            answer_from = database_enquiry(keys)
            while answer_from == 'collision':
                print 'Collision: new key generated'
                total = np.random.randint(1,10000,1) 
                pubkey = np.random.randint(0,total,1)
                prikey = total-pubkey
                keys = {'total': int(total), 'pubkey': int(pubkey), 'prikey': int(prikey)}
                answer_from = database_enquiry(keys)
                if answer_from != 'collision':
                    break
            return answer_from[-1]
            
        
    def PoW(self, claimedprikey, bc, newowner_pk, howmuchbitcoins):
        if bc[0] < howmuchbitcoins:
            print 'Insufficient funds'
            return coins
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
            IDowner = bc1[-1] # pubkey = IDwallet
            
            # Check that newowner_pk is a valid pk (pk's are unique)
            flat_list_pk = []
            for w in blockchain_keys:
                flat_list_pk.append(w['pubkey'])
            if flat_list_pk.count(newowner_pk) == 1:
                
                # Check that claimedprikey is the correct prikey
                totalowner = check(blockchain_keys, IDowner)
                if claimedprikey+bc1[-1] == totalowner:
                    bc1.append(newowner_pk)
                    bc[0] = bc[0] - howmuchbitcoins
                    print 'Transaction accepted'
                    coins.append(bc1) 
                    return coins
                    
                else:
                    print ''' 
                    Your transaction was rejected and unfortunately the reason cannot be disclosed. 
                    A refund has been issued and should appear in your card statement within a few days. 
                    We apologize for the inconvenience. 
                    Actually you just gave us a wrong private key you little piece of mothermary...
                    '''
                    
                    return coins
                    
            else:
                print 'Public key not valid'
                
                return coins
         

      
class wallet(object):
    # Generating keys/wallets so that each key is unique
    # the wallet is already initialized with its keys, as it makes more sense
    def __init__(self):
        self.keys = blockchain().genkey()


class Economies(object):
    
    
    def Wallets_exchange_randomly(self):
       print 'bo'
       
    def Wallets_exchange_wrt_utility_functions(self):
       print 'boo'

# Module
def database_enquiry(keys_new):
        keycheck = []
        for k in blockchain_keys:
            keycheck.append(k['total']-keys_new['total'])   # Remove these two lines to
            keycheck.append(k['prikey']-keys_new['prikey']) # impose uniquness of pubkey only
            keycheck.append(k['pubkey']-keys_new['pubkey'])
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
coins = b.coin 

print 'Input how many wallets you want in the economy (do not choose more than 500)' 
number_of_wallets = raw_input(">")
number_of_wallets = int(number_of_wallets)
steps = np.arange(number_of_wallets)
for steps in steps:
    w = wallet()
    keys = w.keys
    print keys
print blockchain_keys
for k in blockchain_keys:
    coinfor_k = [10 , k['pubkey']]
    coins.append(coinfor_k)
print 'Coins before transaction', coins
wallet_transaction = np.random.randint(0,number_of_wallets,1)
# Begining of the transaction from Wallet_transaction to another Wallet 
IDowner= coins[wallet_transaction][-1]
print 'Transaction from the randomly chosen Wallet ',  IDowner, ' to another Wallet'
print 'Input how much bitcoin you want to transfer?'
Howmuchbitcoins = raw_input(">")
howmuchbitcoins = int(Howmuchbitcoins)
print 'Input the publickey for the new owner' 
newowner_pk = raw_input(">")
newowner_pk = int(newowner_pk)
print 'Input the private key for'
print IDowner
Claimedprikey = raw_input(">")
claimedprikey = int(Claimedprikey)
coins = b.PoW(claimedprikey, coins[wallet_transaction], newowner_pk, howmuchbitcoins)
print 'Coins after transaction economy: [0] = amount, [-1] = pk_owner '
print coins
 



# SOME COMMENTS
# Track wallets balance
# Assign bitcoins to wallets
# impose only public keys to be different
# PoW: need a network and computations that check which bc belongs to who: some ideas: have all wallets denying to have received the bc
# Introduce hash method for chekcing right key
# clash same values in wallets
# TO DO: random wallet generation, cheking unique ID of wallets, create comunication between two wallets in transaction, proof-of-work (PoW)
# coin























