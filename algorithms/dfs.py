import time
from .base_solver import BaseSolver


class DFS(BaseSolver):
    def solve_with_steps(self):
        """DFS with step-by-step visualization data"""
        start_time = time.time()
        stack = [(self.start, [self.start])]
        visited = {self.start}
        steps = []

        while stack:
            current, path = stack.pop()
            steps.append({
                'current': current,
                'visited': visited.copy(),
                'path': path.copy(),
                'stack_size': len(stack)
            })

            if current == self.end:
                end_time = time.time()
                return {
                    'path': path,
                    'nodes_explored': len(visited),
                    'path_length': len(path),
                    'time': end_time - start_time,
                    'algorithm': 'DFS',
                    'steps': steps
                }

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))

        return None
