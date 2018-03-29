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
OBSTACLE_COL = "@"
PATH_COL = "O"

def generate_grid_mulPiece():
    return [list("X------X"), 
            list("--------"), 
            list("-----O--"), 
            list("----@O--"),
            list("--------"),
            list("-----O@-"),
            list("-------@"),
            list("X------X")]

def generate_grid_empty():
    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid_obstacle():
    return [[".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", "#", "#", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid_obstacle_for_b_star():
    """
    worst obstacle for B*
    """

    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def generate_grid_weighted():
    """
    weighted grid
    """

    return [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", "#", "#", "#", ".", "#", "#", "."],
            [".", ".", "2", "1", "9", ".", ".", "#", "."],
            [".", ".", "9", "2", "2", ".", ".", "#", "."],
            [".", ".", "9", "2", "2", ".", ".", "#", "."],
            [".", ".", "2", "9", "9", ".", ".", "#", "."],
            [".", ".", "9", "9", "9", ".", ".", "#", "."],
            [".", "#", "#", "#", "#", "#", "#", "#", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]


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
    neighbors = filter(lambda t: (grid[t[0]][t[1]] != OBSTACLE_COL), neighbors)

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


def init():
    initial_grid = generate_grid_mulPiece()
    start_pos = (6, 4)
    directions = scan_grid(initial_grid, start_pos)

    path1 = find_path(start_pos, (7, 5), directions)
    # need copy as we modify the grid
    grid_with_path1 = draw_path(path1, copy.deepcopy(initial_grid))
    pprint(grid_with_path1)
    print(f"steps: {len(path1)}")
    print(path1)

    path2 = find_path(start_pos, (4, 7), directions)
    grid_with_path2 = draw_path(path2, copy.deepcopy(initial_grid))
    pprint(grid_with_path2)
    print(f"steps: {len(path2)}")
    print(path2)


if __name__ == "__main__":
    init()