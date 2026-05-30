from collections import deque
import time
from .base_solver import BaseSolver


class BFS(BaseSolver):
    def solve_with_steps(self):
        """BFS with step-by-step visualization data"""
        start_time = time.time()
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        steps = []  # Store each exploration step

        while queue:
            current, path = queue.popleft()
            steps.append({
                'current': current,
                'visited': visited.copy(),
                'path': path.copy(),
                'queue_size': len(queue)
            })

            if current == self.end:
                end_time = time.time()
                return {
                    'path': path,
                    'nodes_explored': len(visited),
                    'path_length': len(path),
                    'time': end_time - start_time,
                    'algorithm': 'BFS',
                    'steps': steps
                }

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None
