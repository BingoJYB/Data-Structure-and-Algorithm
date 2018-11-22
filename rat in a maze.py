class Position(object):
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col


def is_safe(maze, pos):
    if pos.row < 0 or pos.row >= len(maze[0]) or pos.col < 0 \
            or pos.col >= len(maze) or maze[pos.row][pos.col] == 0:
        return False
    else:
        return True


def get_path_in_maze(maze, path, pos):
    if path[len(maze[0]) - 1][len(maze) - 1] == 1:
        return True

    for move in [(0, 1), (1, 0)]:
        pos.row += move[0]
        pos.col += move[1]

        if is_safe(maze, pos):
            path[pos.row][pos.col] = 1

            if get_path_in_maze(maze, path, pos):
                return True

            path[pos.row][pos.col] = 0

        pos.row -= move[0]
        pos.col -= move[1]

    return False


pos = Position()
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]
path = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

if get_path_in_maze(maze, path, pos):
    print(path)
else:
    print('Can not find a path!')
