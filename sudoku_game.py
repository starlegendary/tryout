import numpy as np
'''
Goal: create a sudoku game for multi-players
'''
board   = np.full((9,9),0)                                      #define board
format  = [i for i in range(1,10)]
n_given = int(input('Number of Given = '))                      #define number of given position
given   = []                                                    #define given position in form of (橫，直，number)
for i in range(n_given):                                        #ask and change given position in the board
    a = list(map(int,input('Position of Given = ').split(','))) #convert input to integer
    board[a[0],a[1]] = a[2]                                     #convert input to the board
    given.append(a)                                             #store   input to the given
given = np.array(given)                                         #convert given to ndarray
def check(sample):                                              #check if the sample board is correct or not, return True or False
    winx,winy,winm = [False]*3
    for i in range(9):
        winx =     winx and (len(np.unique(sample[i,:]))<9)     #check all 橫 elements
        winy =     winy and (len(np.unique(sample[:,i]))<9)     #check all 直 elements
        for j in range(9):
            winm = winm and (len(np.unique(sample[i*3:i*3+3,j*3:j*3+3]))<9) # check all modules elements
    return winx and winy and winm
def finish(sample):

"""
print(board)
def initial(board,given):
def inn(): #ask input
def outt():
def win(): #check win or not
"""