import numpy as np
import itertools as it
board = np.genfromtxt('tryout.csv',delimiter = ',')
sample = board.copy()

def shift(ls,n):                                          #left shift n-times the elements in the list accordingly 1->0,2->1... by finding
    global sample
    sample = np.where(sample==ls[0], 0            , sample)
    for i in range(1,len(ls)):
        sample = np.where(sample==ls[i],ls[(i+n)%(len(ls))], sample)
    sample = np.where(sample==0    , ls[n%(len(ls))], sample)
order = input().split()
for i in range(1,len(order)):
    order[i] = int(order[i])
if order[0] == 'shift':
    shift(order[2:],order[1])

print(order)
print(sample)