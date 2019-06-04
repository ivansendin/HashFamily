
import numpy as np
import random as R
import math



# wallet size
W_SIZE=32

P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


class HashBits():
    def __init__(self,NUM_HASH,HASH_SIZE):
        ES = int(math.log(HASH_SIZE)/4)
        self.look_up = [ [R.randint(1,W_SIZE-2) for _ in range(ES)] for _ in range(NUM_HASH)]
        self.HASH_SIZE = HASH_SIZE

    def hash(self,w):
        for l in self.look_up:
            yield sum([ ord(w[l[i]])<<(i*4)  for i in range(len(l))])%self.HASH_SIZE
        
class HashNT():
    def __init__(self,NUM_HASH,HASH_SIZE):
        ES = int(math.log(HASH_SIZE)) 
        self.look_up = [[ [R.randint(1,W_SIZE-2),R.choice(P)] for _ in range(ES)] for _ in range(NUM_HASH)]
        self.HASH_SIZE = HASH_SIZE 

    def hash(self,w):
        for l in self.look_up:
            yield sum([ ord(w[_l[0]])*_l[1] for _l in l])%self.HASH_SIZE

def calFilterSizes(n,p):
    m = - (n*math.log(p))/(math.log(2)**2)
    s =  (m/n)/(math.log(2))
    return (m,s)
    
def HashFactory(t,a,b):
    if t=='NT':
        return HashNT(a,b)
    if t=='BITS':
        return HashBits(a,b)
    assert False
    
    
