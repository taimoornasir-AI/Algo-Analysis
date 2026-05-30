import heapq
import time
from .base_solver import BaseSolver


class GreedyBestFirst(BaseSolver):
    def solve_with_steps(self):
        """Greedy Best-First Search with step-by-step visualization data"""
        start_time = time.time()
        heap = [(self.heuristic(self.start), self.start, [self.start])]
        visited = set()
        steps = []

        while heap:
            _, current, path = heapq.heappop(heap)

            if current in visited:
                continue

            visited.add(current)
            steps.append({
                'current': current,
                'visited': visited.copy(),
                'path': path.copy(),
                'heuristic': self.heuristic(current)
            })

            if current == self.end:
                end_time = time.time()
                return {
                    'path': path,
                    'nodes_explored': len(visited),
                    'path_length': len(path),
                    'time': end_time - start_time,
                    'algorithm': 'Greedy Best-First',
                    'steps': steps
                }

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(heap, (self.heuristic(
                        neighbor), neighbor, path + [neighbor]))

        return None
