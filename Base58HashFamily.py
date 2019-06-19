
import numpy as np
import random as R
import math


W_SIZE=32

B58Code = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyzl0'

    
class HashBase58():
    def __init__(self,NUM_HASH,HASH_SIZE):
        #6bits per digit
        ES = int(math.ceil(math.log(HASH_SIZE,2)/6))
        self.look_up_base = [R.randint(1,W_SIZE-2) for _ in range(ES)]
        self.look_up_single = [R.randint(1,W_SIZE-2) for _ in range(NUM_HASH-1)]
        
        self.HASH_SIZE = HASH_SIZE
        self.NUM_HASH = NUM_HASH

    
    def hash(self,w):
        h=0
        for i in range(len(self.look_up_base)):
            h|= B58Code.index(w[ self.look_up_base[i]])<<(i*6)
            
        h = h%self.HASH_SIZE
        yield h%self.HASH_SIZE
        for l in self.look_up_single:
            h= (h<<6 | B58Code.index(w[l]))%self.HASH_SIZE
            yield h
            
