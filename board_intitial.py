
import numpy as np
board = np.full((9,9),0)
print(board)
order = input().split()
for i in range(1,len(order)):
    order[i] = int(order[i])
while  order[0] != 'stop':
    if   order[0] == 'add':
        board[int(order[1]),int(order[2])] = int(order[3])
    elif order[0] == 'shift':
        shift(order[2:],order[1])
    elif order[]
    order = input().split()
print(board)