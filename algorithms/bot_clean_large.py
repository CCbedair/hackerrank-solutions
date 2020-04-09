

cleaned = False
dirt = []
def locateDirt(board):
    global cleaned
    if len(dirt) == 0:
        for index, row in enumerate(board):
            try:
                dirt.append((index, row.index('d')))
            except:
                continue
        dirt.sort()
    if cleaned:
        dirt.pop()
        cleaned = False
    return dirt[0]

def next_move(posx, posy, dimx, dimy, board):
    rpos = (posx, posy)
    dpos = locateDirt(board)
    move = ""
    if rpos == dpos:
        cleaned = True
        move = "CLEAN"
    elif abs(rpos[0] - dpos[0]):
        move = "DOWN" if rpos[0] < dpos[0] else "UP"
    else:
        move = "RIGHT" if rpos[1] < dpos[1]  else "LEFT"
    print(move)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
