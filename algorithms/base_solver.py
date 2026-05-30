import time


class BaseSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])

    def get_neighbors(self, pos):
        row, col = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < self.rows and 0 <= new_col < self.cols and
                    self.maze[new_row][new_col] == 0):
                neighbors.append((new_row, new_col))
        return neighbors

    def heuristic(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])
