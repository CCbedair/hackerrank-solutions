#!/bin/python3

dirt = (-1, -1)
def locateDirt(board):
    if dirt != (-1, -1):
        return dirt
    for index, row in enumerate(board):
        try:
            return (index, row.index('d'))
        except:
            continue
        return (-1, -1)


def nextMove(posr, posc, board):
    rpos = (posr, posc)
    dpos = locateDirt(board)
    move = ""
    if rpos == dpos:
        dirt = (-1, -1)
        move = "CLEAN"
    elif abs(rpos[0] - dpos[0]):
        move = "DOWN" if rpos[0] < dpos[0] else "UP"
    else:
        move = "RIGHT" if rpos[1] < dpos[1]  else "LEFT"
    print(move)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
