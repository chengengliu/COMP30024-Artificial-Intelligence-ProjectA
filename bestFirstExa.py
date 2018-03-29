
from pprint import pprint
from collections import deque
import copy
"""
S - start point
E - end point
x - visited
@ - path
# - obstacle
1 - cost
"""

import math

START_COL = "S"
END_COL = "E"
VISITED_COL = "x"
OBSTACLE_COL = ["@", "O", "X"]
PATH_COL = "P"

def generate_grid_mulPiece():
    return [list("X------X"), 
            list("--------"), 
            list("-----O--"), 
            list("----@O--"),
            list("--------"),
            list("-----O@-"),
            list("-------@"),
            list("X------X")]



def heuristic_distance(pos, end_pos, type="e"):
    """
    m - manhattan
    e - euclidean
    """

    dx = abs(pos[0] - end_pos[0])
    dy = abs(pos[1] - end_pos[1])

    if type == "m":
        return dx + dy

    return math.sqrt(dx * dx + dy * dy)


def find_path(start, end, came_from):
    """Find the shortest path from start to end point"""

    path = [end]

    current = end
    while current != start:
        current = came_from[current]
        path.append(current)

    # reverse to have Start -> Target
    # just looks nicer
    path.reverse()

    return path


def get_cost(grid, pos):
    col_val = grid[pos[0]][pos[1]]
    return int(col_val) if col_val.isdigit() else 1


def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])

    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]

    # make path nicer
    if (row + col) % 2 == 0:
        neighbors.reverse()

    # check borders
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    # check obstacles
    neighbors = filter(lambda t: (grid[t[0]][t[1]] not in OBSTACLE_COL), neighbors)

    return neighbors


def draw_path(path, grid):
    for row, col in path:
        grid[row][col] = PATH_COL

    # draw start and end
    start_pos = path[0]
    end_pos = path[-1]
    grid[start_pos[0]][start_pos[1]] = START_COL
    grid[end_pos[0]][end_pos[1]] = END_COL

    return grid

def scan_grid(grid, start=(0, 0)):
    """Scan all grid, so we can find a path from 'start' to any point"""

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
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                whitePieces.append((i, j))
            if board[i][j] == '@':
                blackPieces.append((i, j))
    
    #to generate path, found out the surrouding enviroment, is it next to a corner or next to a white piece already,
    #or is the piece already at the edge
    for wPiece in whitePieces:
        start_pos = wPiece
        directions = scan_grid(initial_grid, start_pos)
        for bPiece in blackPieces:
            if bPiece[1] == 7 or board[bPiece[0]][bPiece[1]+1] == 'O' or board[bPiece[0]][bPiece[1]+1] == 'X' :
                path = find_path(start_pos, (bPiece[0], bPiece[1]-1), directions)
                grid_with_path = draw_path(path, copy.deepcopy(initial_grid))
                pprint(grid_with_path)
                print(f"steps: {len(path)}")
                print(path)

            elif bPiece[1] == 0 or board[bPiece[0]][bPiece[1]-1] == 'O' or board[bPiece[0]][bPiece[1]-1] == 'X' :
                path = find_path(start_pos, (bPiece[0], bPiece[1]+1), directions)
                grid_with_path = draw_path(path, copy.deepcopy(initial_grid))
                pprint(grid_with_path)
                print(f"steps: {len(path)}")
                print(path)
                
            elif bPiece[0] == 7 or board[bPiece[0]+1][bPiece[1]] == 'O' or board[bPiece[0]+1][bPiece[1]] == 'X' :
                path = find_path(start_pos, (bPiece[0]-1, bPiece[1]), directions)
                grid_with_path = draw_path(path, copy.deepcopy(initial_grid))
                pprint(grid_with_path)
                print(f"steps: {len(path)}")
                print(path)                
                
            elif bPiece[0] == 0 or board[bPiece[0]-1][bPiece[1]] == 'O' or board[bPiece[0]-1][bPiece[1]] == 'X' :
                path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                grid_with_path = draw_path(path, copy.deepcopy(initial_grid))
                pprint(grid_with_path)
                print(f"steps: {len(path)}")
                print(path)                
                
            else:
                path = find_path(start_pos, (bPiece[0]+1, bPiece[1]), directions)
                grid_with_path = draw_path(path, copy.deepcopy(initial_grid))
                pprint(grid_with_path)
                print(f"steps: {len(path)}")
                print(path)


    #start_pos = (4, 6)
    #directions = scan_grid(initial_grid, start_pos)

    #path1 = find_path(start_pos, (5, 7), directions)
    # need copy as we modify the grid
    #grid_with_path1 = draw_path(path1, copy.deepcopy(initial_grid))
    #pprint(grid_with_path1)
    #print(f"steps: {len(path1)}")
    #print(path1)

    '''
    path2 = find_path(start_pos, (4, 7), directions)
    grid_with_path2 = draw_path(path2, copy.deepcopy(initial_grid))
    pprint(grid_with_path2)
    print(f"steps: {len(path2)}")
    print(path2)'''


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