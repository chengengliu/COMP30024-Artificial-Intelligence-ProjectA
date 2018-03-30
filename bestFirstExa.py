from collections import deque
import copy
import math

OBSTACLE_COL = ["@", "O", "X"]

def find_path(start, end, came_from):
    #make the shortest path
    path = [end]

    current = end
    while current != start:
        current = came_from[current]
        path.append(current)

    # reverse to have Start -> Target
    # just looks nicer
    path.reverse()

    return path

def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])

    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]

    # make path nicer
    if (row + col) % 2 == 0:
        neighbors.reverse()

    # check borders
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    # check other pieces
    neighbors = filter(lambda t: (grid[t[0]][t[1]] not in OBSTACLE_COL), neighbors)

    return neighbors

def scan_grid(grid, start=(0, 0)):
    #scan the whole board, so every time we can find a path for the piece put in

    q = deque()
    q.append(start)
    came_from = {start: None}
    while len(q) > 0:
        current_pos = q.popleft()
        neighbors = get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = current_pos

    return came_from


def init(board):
    whitePieces = []
    blackPieces = []
    initial_grid = board
    terminated = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                whitePieces.append((i, j))
            if board[i][j] == '@':
                blackPieces.append((i, j))
    
    #to generate path, found out the surrouding enviroment, is it next to a corner or next to a white piece already,
    #or is the piece already at the edge
    for wPiece in whitePieces:
        for bPiece in blackPieces:
            start_pos = wPiece
            directions = scan_grid(initial_grid, start_pos)
            if bPiece[1] == 7 and board[bPiece[0]][bPiece[1]-1] == 'O':
                terminated.append(bPiece)
            elif board[bPiece[0]-1][bPiece[1]] == 'O' and bPiece[0] == 7:
                terminated.append(bPiece)
            elif board[bPiece[0]+1][bPiece[1]] == 'O'  and bPiece[0] == 0:
                terminated.append(bPiece)
            elif board[bPiece[0]][bPiece[1]-1] == 'O' and bPiece[1] == 0:
                terminated.append(bPiece)        
            elif bPiece[0] != 0 and bPiece[0] != 7 and (board[bPiece[0]-1][bPiece[1]] == 'O' or board[bPiece[0]-1][bPiece[1]] == 'X') and (board[bPiece[0]+1][bPiece[1]] == 'O' or board[bPiece[0]+1][bPiece[1]] == 'X'):
                terminated.append(bPiece)
            elif bPiece[1] != 0 and bPiece[1] != 7 and (board[bPiece[0]][bPiece[1]+1] == 'O' or board[bPiece[0]][bPiece[1]+1] == 'X') and (board[bPiece[0]][bPiece[1]-1] == 'O' or board[bPiece[0]][bPiece[1]-1] == 'X'):
                terminated.append(bPiece)
            if bPiece not in terminated:
                if bPiece[1] == 7 or board[bPiece[0]][bPiece[1]+1] == 'O' or board[bPiece[0]][bPiece[1]+1] == 'X' :
                    path = find_path(start_pos, (bPiece[0], bPiece[1]-1), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    print(f"steps: {len(path)}")
                    print(path)

                elif bPiece[1] == 0 or board[bPiece[0]][bPiece[1]-1] == 'O' or board[bPiece[0]][bPiece[1]-1] == 'X' :
                    path = find_path(start_pos, (bPiece[0], bPiece[1]+1), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    print(f"steps: {len(path)}")
                    print(path)
                        
                elif bPiece[0] == 7 or board[bPiece[0]+1][bPiece[1]] == 'O' or board[bPiece[0]+1][bPiece[1]] == 'X' :
                    path = find_path(start_pos, (bPiece[0]-1, bPiece[1]), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    print(f"steps: {len(path)}")
                    print(path)                
                        
                elif bPiece[0] == 0 or board[bPiece[0]-1][bPiece[1]] == 'O' or board[bPiece[0]-1][bPiece[1]] == 'X' :
                    path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                    terminated.append(bPiece)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    print(f"steps: {len(path)}")
                    print(path)                
                        
                else:
                    path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                    board[wPiece[0]][wPiece[1]] == '-'
                    wPiece = (bPiece[0], bPiece[1]-1)
                    board[wPiece[0]][wPiece[1]] == 'O'
                    print(f"steps: {len(path)}")
                    print(path)


if __name__ == "__main__":
    print("Enter the input, Ctrl+X to end:")
    board = []
    chessBoard = []
    n = 0
    while True:
        try:
             line = input()
        except EOFError:
            break
        board.append(line)
    n = 0
    for line in board:
        if line != "Move" and line != "Massacre":
            #print(line)
            chessBoard.append(line.split(' '))
            n+=1
    init(chessBoard)