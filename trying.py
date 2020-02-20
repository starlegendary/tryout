import numpy as np
import itertools as it
board =  np.genfromtxt('9x9-0001.csv',delimiter = ' ')
sample = np.genfromtxt('tryout.csv'  ,delimiter = ',')

def check(sample):                                              #check if the sample sample is correct or not, return True or False
    winx,winy,winm = [True]*3
    for i in range(3):
        for j in range(3):
            winx = winx and (len(np.unique(sample[i*3+j,:]))==9)     #check all 橫 elements
            winy = winy and (len(np.unique(sample[:,i*3+j]))==9)     #check all 直 elements
            winm = winm and (len(np.unique(sample[i*3:i*3+3,j*3:j*3+3]))==9) # check all modules elements
    return winx and winy and winm
def ele(ls,n):                                               #left shift n-times the elements in the list accordingly 1->0,2->1... by finding
    global sample
    sample = np.where(sample==ls[0], 0            , sample)
    for i in range(1,len(ls)):
        sample = np.where(sample==ls[i],ls[(i+n)%(len(ls))], sample)
    sample = np.where(sample==0    , ls[n%(len(ls))], sample)
def col(ls):
    global sample
    hole = sample[:,ls[0]].copy()
    for i in range(len(ls)-1):
        sample[:,ls[i]] = sample[:,ls[i+1]]
    sample[:,ls[len(ls)-1]] = hole
def row(ls):
    global sample
    hole = sample[ls[0],:].copy()
    for i in range(len(ls)-1):
        sample[ls[i],:] = sample[ls[i+1],:]
    sample[ls[len(ls)-1],:] = hole

def ex_ele(a,b):
    global sample
    for i in range(len(a)):
        ele([a[i],b[i]+10],1)
    sample[sample>10] = sample[sample>10] - 10
a = list( board[0:3,0:3])
b = list(sample[0:3,0:3])
i = 0
j = 1

print(sample)

ex_ele(a,b)


ex_ele([6,1,7],[1,7,6])

print(check(sample))
print(sample)
print((board == sample).sum()) #parameter of algorithm for similar or not