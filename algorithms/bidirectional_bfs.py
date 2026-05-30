from collections import deque
import time
from .base_solver import BaseSolver


class BidirectionalBFS(BaseSolver):
    def solve_with_steps(self):
        """Bidirectional BFS with step-by-step visualization data"""
        start_time = time.time()
        start_queue = deque([(self.start, [self.start])])
        end_queue = deque([(self.end, [self.end])])
        start_visited = {self.start}
        end_visited = {self.end}
        start_parent = {self.start: None}
        end_parent = {self.end: None}
        steps = []

        while start_queue and end_queue:
            # Forward search
            current_start, path_start = start_queue.popleft()
            steps.append({
                'current': current_start,
                'visited': start_visited.copy(),
                'path': path_start.copy(),
                'direction': 'forward'
            })

            for neighbor in self.get_neighbors(current_start):
                if neighbor not in start_visited:
                    start_visited.add(neighbor)
                    start_queue.append((neighbor, path_start + [neighbor]))
                    start_parent[neighbor] = current_start

                    if neighbor in end_visited:
                        # Found intersection
                        end_time = time.time()
                        # Reconstruct path
                        path = self._reconstruct_path(
                            start_parent, end_parent, neighbor)
                        return {
                            'path': path,
                            'nodes_explored': len(start_visited) + len(end_visited),
                            'path_length': len(path),
                            'time': end_time - start_time,
                            'algorithm': 'Bidirectional BFS',
                            'steps': steps
                        }

            # Backward search
            current_end, path_end = end_queue.popleft()
            steps.append({
                'current': current_end,
                'visited': end_visited.copy(),
                'path': path_end.copy(),
                'direction': 'backward'
            })

            for neighbor in self.get_neighbors(current_end):
                if neighbor not in end_visited:
                    end_visited.add(neighbor)
                    end_queue.append((neighbor, path_end + [neighbor]))
                    end_parent[neighbor] = current_end

                    if neighbor in start_visited:
                        # Found intersection
                        end_time = time.time()
                        # Reconstruct path
                        path = self._reconstruct_path(
                            start_parent, end_parent, neighbor)
                        return {
                            'path': path,
                            'nodes_explored': len(start_visited) + len(end_visited),
                            'path_length': len(path),
                            'time': end_time - start_time,
                            'algorithm': 'Bidirectional BFS',
                            'steps': steps
                        }

        return None

    def _reconstruct_path(self, start_parent, end_parent, meeting_point):
        """Reconstruct the path from start to end through meeting point"""
        # Path from start to meeting point
        path_start = []
        current = meeting_point
        while current is not None:
            path_start.append(current)
            current = start_parent.get(current)
        path_start.reverse()

        # Path from meeting point to end (excluding meeting point)
        path_end = []
        current = end_parent.get(meeting_point)
        while current is not None:
            path_end.append(current)
            current = end_parent.get(current)

        return path_start + path_end
