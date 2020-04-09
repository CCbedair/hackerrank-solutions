#!/usr/bin/python

def index2d(elem, grid):
    for i, row in enumerate(grid):
        try:
            return (i, row.index(elem))
        except:
            continue
    return (-1, -1)


def displayPathtoPrincess(n,grid):
#print all the moves here
    ppos = index2d('p', grid)
    mpos = index2d('m', grid)
    xprint = "RIGHT\n" if mpos[1] < ppos[1] else "LEFT\n"
    yprint = "DOWN\n" if mpos[0] < ppos[0] else "UP\n"
    print(xprint * abs(ppos[0] - mpos[0]), end='')
    print(yprint * abs(ppos[1] - mpos[1]), end='')

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
