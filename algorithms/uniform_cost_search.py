import heapq
import time
from .base_solver import BaseSolver


class UniformCostSearch(BaseSolver):
    def solve_with_steps(self):
        """Uniform Cost Search with step-by-step visualization data"""
        start_time = time.time()
        heap = [(0, self.start, [self.start])]
        visited = set()
        cost_so_far = {self.start: 0}
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
                    'algorithm': 'Uniform Cost Search',
                    'steps': steps
                }

            for neighbor in self.get_neighbors(current):
                new_cost = cost + 1  # Uniform cost of 1 per step
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(
                        heap, (new_cost, neighbor, path + [neighbor]))

        return None
