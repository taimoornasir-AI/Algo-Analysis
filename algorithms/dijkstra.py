import heapq
import time
from .base_solver import BaseSolver


class Dijkstra(BaseSolver):
    def solve_with_steps(self):
        """Dijkstra with step-by-step visualization data"""
        start_time = time.time()
        heap = [(0, self.start, [self.start])]
        visited = set()
        steps = []

        while heap:
            cost, current, path = heapq.heappop(heap)

            if current in visited:
                continue

            visited.add(current)
            steps.append({
                'current': current,
                'visited': visited.copy(),
                'path': path.copy(),
                'cost': cost
            })

            if current == self.end:
                end_time = time.time()
                return {
                    'path': path,
                    'nodes_explored': len(visited),
                    'path_length': len(path),
                    'time': end_time - start_time,
                    'algorithm': 'Dijkstra',
                    'steps': steps
                }

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(
                        heap, (cost + 1, neighbor, path + [neighbor]))

        return None
