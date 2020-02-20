'''
Create all possible partions of 3 elements in a 3x3 module where rotate and exchange of the module will be seen as the same element.
Create sudoku through partition
'''
import numpy as np
import itertools as it
from generator import sudoku

board = np.genfromtxt('tryout.csv', delimiter=',')
sample = np.genfromtxt('9x9-0003.csv', delimiter=' ')

def module(board, i):
    a, b = (i-1)//3, (i-1) % 3
    return board[a*3:a*3+3, b*3:b*3+3]
def party(a,m,n): 
    b = [[], []]
    for i in range(len(a)):
        b[0].append(np.sum(a[i,a[i,:] <= n]>=m))
        b[1].append(np.sum(a[a[:,i] <= n,i]>=m))
    return b

sample = sudoku(3)
sample2 = sudoku(3)

print(sample)

for i in range(1,10):
    print(i)
    for n in range(3):
        print(party(module(sample, i),n*3+1, n*3+3))
        print(party(module(sample2, i),n*3+1, n*3+3))
    print('')

