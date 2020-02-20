import numpy as np
from itertools import combinations as com
from itertools import permutations as per
board = np.genfromtxt('tryout.csv',delimiter = ',')
sample = board.copy()

o = [True]*3
x = [False]*3
o1 = [True,False,False]
ooo = np.array((o+o+o))
oxx = np.array((o+x+x))
xox = np.array((x+o+x))
xxo = np.array((x+x+o))
xxx = np.array((x+x+x))
coloxx = np.array(([oxx,xxx,xxx]*3))
wal = np.array((o1*3))
def check(sample):                                              #check if the sample sample is correct or not, return True or False
    winx,winy,winm = [True]*3
    for i in range(3):
        for j in range(3):
            winx = winx and (len(np.unique(sample[i*3+j,:]))==9)     #check all 橫 elements
            winy = winy and (len(np.unique(sample[:,i*3+j]))==9)     #check all 直 elements
            winm = winm and (len(np.unique(sample[i*3:i*3+3,j*3:j*3+3]))==9) # check all modules elements
    return winx and winy and winm
def shift(ls,n):                                               #left shift n-times the elements in the list accordingly 1->0,2->1... by finding
    global sample
    sample = np.where(sample==ls[0], 0            , sample)
    for i in range(1,len(ls)):
        sample = np.where(sample==ls[i],ls[(i+n)%(len(ls))], sample)
    sample = np.where(sample==0    , ls[n%(len(ls))], sample)
def row3(i):                                             #shift 3 rows
    global sample
    hole = sample[i,:].copy()
    sample[i+0,:] = sample[i+1,:]
    sample[i+1,:] = sample[i+2,:]
    sample[i+2,:] = hole
def col(ls):
    global sample
    hole = sample[ls[0],:].copy()
    for i in range(len(ls)-1):
        sample[ls[i],:] = sample[ls[i+1],:]
    sample[ls[len(ls)-1],:] = hole
def wal_col(i,sample):                                          #shift elements in 3 walls in 3 columns
    hole = sample[wal,i].copy()
    sample[wal,i  ] = sample[wal,i+1]
    sample[wal,i+1] = sample[wal,i+2]
    sample[wal,i+3] = hole
def wal_row(i,sample):                                          #shift elements in 3 walls in 3 rows

    hole = sample[0,wal].copy()
    sample[i  ,wal] = sample[i+1,wal]
    sample[i+1,wal] = sample[i+2,wal]
    sample[i+2,wal] = hole
def rotate()

shift([1,2])
shift([7,6])
shift([9,3])
print(sample)
print(check(sample))