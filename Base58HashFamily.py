
import numpy as np
import random as R
import math


W_SIZE=32

B58Code = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyzl0'

    
class HashBase58():
    def __init__(self,NUM_HASH,HASH_SIZE):
        #6bits per digit
        ES = int(math.ceil(math.log(HASH_SIZE,2)/6))
        self.look_up = [ [R.randint(1,W_SIZE-2) for _ in range(ES)] for _ in range(NUM_HASH)]
        self.HASH_SIZE = HASH_SIZE

    def hash(self,w):
        for l in self.look_up:
            h=0
            for i in range(len(l)):
                h|= B58Code.index(w[l[i]])<<(i*6)
            yield h%self.HASH_SIZE
    
