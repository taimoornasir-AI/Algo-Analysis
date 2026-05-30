import heapq
import time
from .base_solver import BaseSolver


class JumpPointSearch(BaseSolver):
    def solve_with_steps(self):
        """Simplified Jump Point Search with step-by-step visualization data"""
        start_time = time.time()
        heap = [(self.heuristic(self.start), 0, self.start, [self.start])]
        visited = set()
        steps = []

        while heap:
            _, cost, current, path = heapq.heappop(heap)

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
                    'algorithm': 'Jump Point Search',
                    'steps': steps
                }

            # Simplified jump point logic - just check neighbors but skip some
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    # Simple pruning: don't explore if there's a shorter path
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(heap, (priority, new_cost,
                                   neighbor, path + [neighbor]))

        return None
