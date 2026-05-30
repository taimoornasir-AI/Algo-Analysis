import random


class MazeGenerator:
    def __init__(self, width=20, height=20, loop_factor=0.15):
        self.width = width
        self.height = height
        self.loop_factor = loop_factor
        self.maze = [[1 for _ in range(width * 2 + 1)]
                     for _ in range(height * 2 + 1)]

    def generate(self):
        stack = []
        start_x, start_y = 0, 0
        self.maze[start_y * 2 + 1][start_x * 2 + 1] = 0
        stack.append((start_x, start_y))

        while stack:
            x, y = stack[-1]
            neighbors = self._get_unvisited_neighbors(x, y)

            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x = x * 2 + 1 + (next_x - x)
                wall_y = y * 2 + 1 + (next_y - y)
                self.maze[wall_y][wall_x] = 0
                self.maze[next_y * 2 + 1][next_x * 2 + 1] = 0
                stack.append((next_x, next_y))
            else:
                stack.pop()

        self._add_loops()
        return self.maze

    def _add_loops(self):
        wall_positions = []
        for i in range(1, len(self.maze) - 1):
            for j in range(1, len(self.maze[0]) - 1):
                if self.maze[i][j] == 1 and self._is_removable_wall(i, j):
                    wall_positions.append((i, j))

        num_walls_to_remove = int(len(wall_positions) * self.loop_factor)
        walls_to_remove = random.sample(wall_positions, min(
            num_walls_to_remove, len(wall_positions)))

        for i, j in walls_to_remove:
            self.maze[i][j] = 0

    def _is_removable_wall(self, i, j):
        if (i > 0 and i < len(self.maze) - 1 and
                self.maze[i-1][j] == 0 and self.maze[i+1][j] == 0):
            return True
        if (j > 0 and j < len(self.maze[0]) - 1 and
                self.maze[i][j-1] == 0 and self.maze[i][j+1] == 0):
            return True
        return False

    def _get_unvisited_neighbors(self, x, y):
        neighbors = []
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.width and 0 <= ny < self.height and
                    self.maze[ny * 2 + 1][nx * 2 + 1] == 1):
                neighbors.append((nx, ny))

        return neighbors

    def add_entrance_exit(self):
        self.maze[0][1] = 0
        self.start = (0, 1)
        self.maze[-1][-2] = 0
        self.end = (len(self.maze) - 1, len(self.maze[0]) - 2)
