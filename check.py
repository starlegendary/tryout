import numpy as np
board = np.genfromtxt('tryout.csv',delimiter = ',')
sample = board.copy()
def check(sample):                                              #check if the sample board is correct or not, return True or False
    winx,winy,winm = [True]*3
    for i in range(3):
        for j in range(3):
            winx = winx and (len(np.unique(sample[i*3+j,:]))==9)     #check all 橫 elements
            winy = winy and (len(np.unique(sample[:,i*3+j]))==9)     #check all 直 elements
            winm = winm and (len(np.unique(sample[i*3:i*3+3,j*3:j*3+3]))==9) # check all modules elements
    return winx and winy and winm
print(board)
def shift(ls,n):                                               #left shift n-times the elements in the list accordingly 1->0,2->1... by finding
    global sample
    sample = np.where(sample==ls[0], 0            , sample)
    for i in range(1,len(ls)):
        sample = np.where(sample==ls[i],ls[(i+n)%(len(ls))], sample)
    sample = np.where(sample==0    , ls[n%(len(ls))], sample)
print(check(board))
shift([1,2,4],2)
print(sample)
