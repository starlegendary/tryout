import numpy as np
'''
Goal: create a series of true false responsible for diff move
'''
from itertools import combinations as com
from itertools import permutations as per
board = np.genfromtxt('tryout.csv',delimiter = ',')
o = [True]*3
x = [False]*3
o1 = [True,False,False]
ooo = np.array((o+o+o))
oxx = np.array((o+x+x))
xox = np.array((x+o+x))
xxo = np.array((x+x+o))
xxx = np.array((x+x+x))
coloxx = np.array(([oxx,xxx,xxx]*3))
from partitions import module
print(module(board,1))