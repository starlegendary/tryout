import numpy  as np
from random import sample

# pattern for a baseline valid solution
def pattern(r,c,base): return (base*(r%base)+r//base+c)%(base**2)

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 

def sudoku(base):
    rows  = [ g*base + r for g in shuffle(range(base)) for r in shuffle(range(base)) ] 
    cols  = [ g*base + c for g in shuffle(range(base)) for c in shuffle(range(base)) ]
    nums  = shuffle(range(1,base**2+1))
    # produce board using randomized baseline pattern

    return np.array([ [nums[pattern(r,c,base)] for c in cols] for r in rows ])
print(sudoku(3))

import csv

with open('9x9-0005.csv', 'w', newline='') as myfile:
    a = csv.writer(myfile, delimiter = ',')
    data = sudoku(3)
    a.writerow(data)