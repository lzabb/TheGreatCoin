# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:49:46 2017

@author: Mas
"""


class blockchain(object):
    
   
    def __init__(self):
        self.blockchain_keys = []
        self.coins = []
    
    #moved the setting of a =  100 here as it should be a characteristic of the genkey funtion,
   #decoupled from the wallet object
    def genkey(self):
         
        
        prikey = ''.join(random.choice('0123456789ABCDEFghij') for i in range(16))
        pubkey = hash(prikey)
        keys = {'pubkey': pubkey, 'prikey': prikey}
        if blockchain_keys == []:
            blockchain_keys.append(keys)
            return keys
        else:
            def database_enquiry(keys_new):
                keycheck = []
                for k in blockchain_keys:
                    #keycheck.append(k['total']-keys_new['total'])   # Remove these two lines to
                    #keycheck.append(k['prikey']-keys_new['prikey']) # impose uniquness of pubkey only
                    if k['pubkey'] == keys_new['pubkey']:
                        keycheck.append(0)
                    else:
                        keycheck.append(1)
                if keycheck.count(0) >= 1:
                    return 'collision'
                else:
                    blockchain_keys.append(keys_new)
                    return blockchain_keys
                    print keys_new
            answer_from = database_enquiry(keys)
            while answer_from == 'collision':
                print 'Collision: new key generated'
                prikey = ''.join(random.choice('0123456789ABCDEFghij') for i in range(16))
                pubkey = hash(prikey)
                keys = {'pubkey': pubkey, 'prikey': prikey}
                answer_from = database_enquiry(keys)
                if answer_from != 'collision':
                    break
            return answer_from[-1]
            
        
    def PoW(self, claimedprikey, bc, newowner_pk, howmuchbitcoins):
        if bc[0] < howmuchbitcoins:
            print 'Insufficient funds'
            return coins
        else:
           
                
            # New bitcoin created        
            bc1 = list(bc)
            bc1[0] = howmuchbitcoins
            IDowner = bc1[-1] # pubkey = IDwallet
            
            # Check that newowner_pk is a valid pk (pk's are unique)
            flat_list_pk = []
            
            for w in blockchain_keys:
                flat_list_pk.append(int(w['pubkey']))
                
            if flat_list_pk.count(int(newowner_pk)) == 1:
                
                # Check that claimedprikey is the correct prikey
                #prikey_owner = check(blockchain_keys, IDowner) KEYMOMENT WHERE NO NEED FOR A PRIKEY DATABASE IS NEEDED
                if hash(claimedprikey) == IDowner:
                    # Work
                    start = time.time()
                    answer = np.random.randint(0,10000,1)
                    answer = int(answer) 
                    print answer
                    while answer != 0:
                        
                        b = np.random.randint(0,10000,1)  
                        b = int(b) 
                        answer = b
                        if answer == 0:
                            break
                    end = time.time()
                    elapsed = end - start
                    print 'Time worked by node ZERO :', elapsed
                    bc1.append(newowner_pk)
                    bc1.append(elapsed)
                    bc[0] = bc[0] - howmuchbitcoins
                    print 'Transaction accepted by node ZERO', 
                    coins.append(bc1) 
                    print bc1
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
                
    def PoW_1stblock(self, claimedprikey, bc, newowner_pk, howmuchbitcoins):
        if bc[0] < howmuchbitcoins:
            print 'Insufficient funds'
            return coins
        else:
              
            # New bitcoin created        
            block = list(bc)
            block[0] = howmuchbitcoins
            IDowner = block[1] # pubkey = IDwallet
            
            # Check that newowner_pk is a valid pk (pk's are unique)
            flat_list_pk = []
            for w in blockchain_keys:
                flat_list_pk.append(int(w['pubkey']))
                
            if flat_list_pk.count(int(newowner_pk)) == 1:
                
                # Check that claimedprikey is the correct prikey
                #prikey_owner = check(blockchain_keys, IDowner) KEYMOMENT WHERE NO NEED FOR A PRIKEY DATABASE IS NEEDED
                if hash(claimedprikey) == IDowner:
                    # work
                    start = time.time()
                    answer = np.random.randint(0,10000,1)
                    answer = int(answer) 
                    
                    while answer != 0:
                        
                        b = np.random.randint(0,10000,1)  
                        b = int(b) 
                        answer = b
                        if answer == 0:
                            break
                    end = time.time()
                    elapsed = end - start
                    print 'Time worked by node ZERO :', elapsed,'.'
                    block.append(newowner_pk)
                    block.append(elapsed)
                    block.append('block start')
                    
                    
                    print 'Transaction accepted by node ZERO .', 
                    coins.append(block) 
                    print 'Block:', block
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

                
    def PoW_on_block(self, claimedprikey, bc, newowner_pk, howmuchbitcoins, k):
        if bc[0] < howmuchbitcoins:
            print 'transaction Denied'
            block.append('Denied')
            return block
        else:
            
                
            # New bitcoin created        
            
            IDowner = block[1] # pubkey = IDwallet
            
            # Check that newowner_pk is a valid pk (pk's are unique)
            flat_list_pk = []
            
            for w in blockchain_keys:
                flat_list_pk.append(int(w['pubkey']))
                
            if flat_list_pk.count(int(newowner_pk)) == 1:
                
                # Check that claimedprikey is the correct prikey
                #prikey_owner = check(blockchain_keys, IDowner) KEYMOMENT WHERE NO NEED FOR A PRIKEY DATABASE IS NEEDED
                if hash(claimedprikey) == IDowner:
             
               
                    # Work: exexute operation with probability of success of 10^{-5}
                    start = time.time()
                    answer = np.random.randint(0,10000,1)
                    answer = int(answer) 
                    
                    while answer != 0:
                        
                        b = np.random.randint(0,10000,1)  
                        b = int(b) 
                        answer = b
                        if answer == 0:
                            break
                    end = time.time()
                    elapsed = end - start
                    print 'Time worked by node ', k['pubkey'],':', elapsed,'.'
                    
                    block.append(elapsed)
                    block.append(k['pubkey'])
                    nodeswork.append([k['pubkey'],elapsed])
                    
                    print 'Transaction accepted by node', k['pubkey'],'.'
                     
                    print 'Block updated.', #block
                    return block
                    
                else:
                    print ''' 
                    Invalid private key you little piece of mothermary...
                    '''
                    
                    block.append('Denied')
                    block.append(k['pubkey'])
                    return block
                    
            else:
                print 'Public key not valid'
                block.append('Denied')
                block.append(k['pubkey'])
                return block
         


      
class wallet(object):
    # Generating keys/wallets so that each key is unique
    # the wallet is already initialized with its keys, as it makes more sense
    def __init__(self):
        self.keys = blockchain().genkey()


class economies(object): # Plan to introduce different possible generation/interactions for wallets
    
    
    def Wnum_randWowner_detWrecepient_1tr_detbc(self):
        print 'Input how many wallets you want in the economy (choose less thann 500) (each wallet gets assigned 10 bitcoins):' 
        number_of_wallets = raw_input(">")
        number_of_wallets = int(number_of_wallets)
        steps = np.arange(number_of_wallets)
        for steps in steps:
            w = wallet()
            keys = w.keys
            print keys
        print 'blockchain_keys:', blockchain_keys
        for k in blockchain_keys:
            coinfor_k = [10 , k['pubkey']]
            coins.append(coinfor_k)
        print 'Coins before transaction:', coins
        wallet_transaction = np.random.randint(0,number_of_wallets,1)
        # Begining of the transaction from Wallet_transaction to another Wallet 
        IDowner = coins[int(wallet_transaction)][-1]
        print '-------------BEGINING OF TRANSACTION--------------'
        print 'Transaction from the randomly chosen Wallet: pubkey =',  IDowner, '.'
        print 'Input how much bitcoin you want to transfer:'
        Howmuchbitcoins = raw_input(">")
        howmuchbitcoins = int(Howmuchbitcoins)
        print 'Input the publickey for the new owner' 
        newowner_pk = raw_input(">")
        #newowner_pk = int(newowner_pk)
        print 'Input the private key for:'
        print 'Wallet:', IDowner
        print  '(suggestion ', blockchain_keys[int(wallet_transaction)]['prikey'],')'
        claimedprikey = raw_input(">")
        #claimedprikey = int(claimedprikey)
        b.PoW(claimedprikey, coins[int(wallet_transaction)], newowner_pk, howmuchbitcoins)
        print 'Coins after transaction: ([0] = amount, [-1] = pk_owner): '
        print coins
        
        
    def nodes_work(self):
       
       #need to input previous valued that input in previous function, then run PoW   
       #nodes creation for each
       print '-------------BEGINING OF VOTING/WORK ON BLOCK--------------'
       for k in blockchain_keys:
           Block = b.PoW_on_block(claimedprikey, bc, newowner_pk, howmuchbitcoins,k)
         
       block = Block
       return block

    def Wnum_auto1tr_ran(self):
        print '---------------------------'
        print 'Input how many wallets you want in the economy (choose less thann 500) (each wallet gets assigned 10 bitcoins):' 
        number_of_wallets = raw_input(">")
        number_of_wallets = int(number_of_wallets)
        steps = np.arange(number_of_wallets)
        for steps in steps:
            wallet()
            #keys = w.keys
            #print keys
        #print 'blockchain_keys:', blockchain_keys
        for k in blockchain_keys:
            coinfor_k = [10 , k['pubkey']]
            coins.append(coinfor_k)
        print 'Coins before transaction:', coins
        wallet_transaction = np.random.randint(0,number_of_wallets,1)
        # Begining of the transaction from Wallet_transaction to another Wallet 
        IDowner = coins[int(wallet_transaction)][-1]
        print '-------------BEGINING OF TRANSACTION AND BLOCK CREATION--------------'
        print 'Transaction from the randomly chosen Wallet: pubkey =',  IDowner, '.'
        #print 'Input how much bitcoin you want to transfer:'
        Howmuchbitcoins = np.random.randint(1,9,1)
        howmuchbitcoins = int(Howmuchbitcoins)
        print 'Randomly chosen amount to transfer:',howmuchbitcoins,'.'

        #print 'Input the publickey for the new owner' 
        newowner_pk = np.random.randint(0,number_of_wallets,1)
        newowner_pk = blockchain_keys[int(newowner_pk)]['pubkey']
        print 'Randomly chosen recipient: publickey =',newowner_pk,'.'
        print 'Input the private key for:'
        print 'Wallet:', IDowner
        print  '(suggestion ', blockchain_keys[int(wallet_transaction)]['prikey'],')'
        claimedprikey = raw_input(">")
        #claimedprikey = int(claimedprikey)
        b.PoW_1stblock(claimedprikey, coins[int(wallet_transaction)], newowner_pk, howmuchbitcoins)
        print 'Coins after transaction: ([0] = amount, [-1] = pk_owner): '
        print coins
        block = coins[-1]
        nodeswork = []
        output = [block, claimedprikey, coins[int(wallet_transaction)], newowner_pk, howmuchbitcoins, nodeswork]
        return output
       
    def Wallets_exchange_wrt_utility_functions(self):
       print 'tbd'


class stats(object):
    def __init__(self):
        #Some stats on working time
        if nodeswork != []:
            tot_work = 0
            l = len(block)
            l = np.arange(l) 
            for l in l:
                if l <= 4:
                    pass
                else:
                    remainder = l % 2 #The time worked by each node is found on the odd entries of the list block for entries greater than block[4]
                    if remainder == 0:
                        pass
                    else:
                        tot_work = tot_work + block[l]
            print 'Total time worked on the block:', tot_work,'.'
            
            ma= max(nodeswork, key=lambda item: item[1])
            mi = min(nodeswork, key=lambda item: item[1])
            #check
            for i in nodeswork:
                if i[1] <= mi[1]:
                    pass
                else:
                    'not max'
            print 'Maximum work (the node in [0]):', ma,'.'
            print 'Minimum work (the node in [0]):', mi,'.'
            
            av = tot_work / len(nodeswork)
            v = []
            for i in nodeswork:
                v.append((i[1]-av)*(i[1]-av)/len(nodeswork))
            sd = math.sqrt(sum(v))
            sd_normaliser = max([ma[1] - av, av - mi[1]])
            print 'Average of work:', av,'.'
            print 'Standard deviation of work:', sd,'.'
            if sd_normaliser != 0:
                nsd = sd / sd_normaliser
                print 'Normalised standard deviation of work: ', nsd,'.'
            else: pass
        else:
            print 'No stats.'

            



    
    #BEGIN
import numpy as np
import time
import math
import random

b = blockchain()
blockchain_keys = b.blockchain_keys
coins = b.coins 
e = economies()
#output = e.Wnum_randWowner_detWrecepient_1tr_detbc()
output = e.Wnum_auto1tr_ran() #first automatic transaction (only imput privatekey) and block is generated
block = output[0]
claimedprikey =  output[1]
bc =  output[2]
newowner_pk =  output[3]
howmuchbitcoins =  output[4]
nodeswork = output[5]
block = e.nodes_work() # the block is updated as nodes (same as wallets) confirm the transaction going through work
print '-------------STATS-------------'
stats()       
        
     
    


# SOME COMMENTS
# Track wallets balance
# TO DO:  create comunication between two wallets in transaction (utility functions), proof-of-work (PoW)
