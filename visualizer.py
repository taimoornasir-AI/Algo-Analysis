import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from matplotlib.animation import FuncAnimation


class AnimatedMazeVisualizer:
    def __init__(self, maze, start, end):
        self.maze = np.array(maze)
        self.start = start
        self.end = end

    def animate_solution(self, result):
        """Animate the algorithm solving the maze"""
        if not result or 'steps' not in result:
            print("No solution found!")
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

        # Setup maze visualization
        grass_color = '#2d5016'
        path_color = '#ffffff'
        colors = [path_color, grass_color]
        cmap = LinearSegmentedColormap.from_list('maze', colors, N=2)

        ax1.imshow(self.maze, cmap=cmap, interpolation='nearest')
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.set_title(f'{result["algorithm"]} - Solving...',
                      fontsize=14, fontweight='bold')

        # Start and end markers
        start_circle = patches.Circle((self.start[1], self.start[0]),
                                      radius=0.5, color='lime', zorder=10)
        ax1.add_patch(start_circle)
        ax1.text(self.start[1], self.start[0], 'S',
                 ha='center', va='center', fontsize=10,
                 fontweight='bold', color='black', zorder=11)

        end_circle = patches.Circle((self.end[1], self.end[0]),
                                    radius=0.5, color='red', zorder=10)
        ax1.add_patch(end_circle)
        ax1.text(self.end[1], self.end[0], 'E',
                 ha='center', va='center', fontsize=10,
                 fontweight='bold', color='white', zorder=11)

        # Initialize plot elements
        visited_scatter = ax1.scatter(
            [], [], c='cyan', s=20, alpha=0.3, zorder=3)
        current_scatter = ax1.scatter(
            [], [], c='yellow', s=100, marker='*', zorder=5)
        path_line, = ax1.plot([], [], 'b-', linewidth=2, alpha=0.6, zorder=4)

        # Info panel
        ax2.axis('off')
        info_text = ax2.text(0.1, 0.9, '', fontsize=12, verticalalignment='top',
                             family='monospace', wrap=True)

        steps = result['steps']

        def init():
            visited_scatter.set_offsets(np.empty((0, 2)))
            current_scatter.set_offsets(np.empty((0, 2)))
            path_line.set_data([], [])
            return visited_scatter, current_scatter, path_line, info_text

        def update(frame):
            if frame >= len(steps):
                frame = len(steps) - 1

            step = steps[frame]

            # Update visited nodes
            visited_list = list(step['visited'])
            if visited_list:
                visited_array = np.array([[p[1], p[0]] for p in visited_list])
                visited_scatter.set_offsets(visited_array)

            # Update current node
            current = step['current']
            current_scatter.set_offsets([[current[1], current[0]]])

            # Update path
            path = step['path']
            if len(path) > 1:
                path_y = [p[0] for p in path]
                path_x = [p[1] for p in path]
                path_line.set_data(path_x, path_y)

            # Update info text
            info = f"""
{result['algorithm']} ALGORITHM

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROGRESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step: {frame + 1} / {len(steps)}
Nodes Explored: {len(step['visited'])}
Current Path Length: {len(step['path'])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

            if frame == len(steps) - 1:
                info += f"""✅ SOLUTION FOUND!

Final Path Length: {result['path_length']}
Total Nodes Explored: {result['nodes_explored']}
Time Taken: {result['time']*1000:.2f} ms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            else:
                info += f"""🔍 Searching...

Current Position: {current}
"""

            info_text.set_text(info)

            return visited_scatter, current_scatter, path_line, info_text

        # Calculate animation speed based on number of steps
        interval = max(50, min(500, 10000 // len(steps)))

        anim = FuncAnimation(fig, update, frames=len(steps), init_func=init,
                             interval=interval, blit=True, repeat=False)

        plt.tight_layout()
        plt.show()

        # Show final explanation
        self.show_explanation(result)

    def show_explanation(self, result):
        """Show detailed explanation after animation"""
        algo = result['algorithm']

        explanations = {
            'BFS': {
                'name': 'Breadth-First Search (BFS)',
                'description': 'Explores the maze level by level, like ripples in water.',
                'how_it_works': [
                    '1. Starts at the entrance',
                    '2. Explores all neighbors at current distance',
                    '3. Then moves to next distance level',
                    '4. Continues until exit is found'
                ],
                'guarantees': 'Always finds the SHORTEST path',
                'best_for': 'When you need the optimal solution',
                'time_complexity': 'O(V + E) where V=vertices, E=edges',
                'space_complexity': 'O(V) - stores all nodes at current level'
            },
            'DFS': {
                'name': 'Depth-First Search (DFS)',
                'description': 'Explores as far as possible along each branch before backtracking.',
                'how_it_works': [
                    '1. Starts at the entrance',
                    '2. Picks a direction and goes as deep as possible',
                    '3. Backtracks when hitting dead ends',
                    '4. Continues until exit is found'
                ],
                'guarantees': 'Finds A path, but NOT always the shortest',
                'best_for': 'When memory is limited or exploring possibilities',
                'time_complexity': 'O(V + E) where V=vertices, E=edges',
                'space_complexity': 'O(h) where h=height - uses less memory'
            },
            'Dijkstra': {
                'name': "Dijkstra's Algorithm",
                'description': 'Finds shortest path by keeping track of distances from start.',
                'how_it_works': [
                    '1. Assigns distance 0 to start, infinity to others',
                    '2. Always explores the closest unvisited node',
                    '3. Updates distances to neighbors',
                    '4. Continues until exit is reached'
                ],
                'guarantees': 'Always finds the SHORTEST path with weighted edges',
                'best_for': 'Graphs with different edge costs (same as BFS for mazes)',
                'time_complexity': 'O((V + E) log V) with priority queue',
                'space_complexity': 'O(V) - stores distances for all nodes'
            },
            'A*': {
                'name': 'A* (A-Star) Algorithm',
                'description': 'Smart search that uses a heuristic to guide exploration toward the goal.',
                'how_it_works': [
                    '1. Combines actual distance + estimated distance to goal',
                    '2. Always explores most promising nodes first',
                    '3. Uses Manhattan distance as heuristic',
                    '4. Reaches goal more efficiently'
                ],
                'guarantees': 'Finds SHORTEST path while exploring fewer nodes',
                'best_for': 'When you want optimal path AND efficiency',
                'time_complexity': 'O((V + E) log V) but explores fewer nodes',
                'space_complexity': 'O(V) - stores nodes in priority queue'
            },
            'Greedy Best-First': {
                'name': 'Greedy Best-First Search',
                'description': 'Always explores the node that appears closest to the goal.',
                'how_it_works': [
                    '1. Uses only heuristic (estimated distance to goal)',
                    '2. Always picks the most promising node',
                    '3. Ignores actual distance traveled',
                    '4. Can get stuck in loops or suboptimal paths'
                ],
                'guarantees': 'Finds A path quickly, but NOT optimal',
                'best_for': 'When speed matters more than optimality',
                'time_complexity': 'O(V + E) worst case, often better',
                'space_complexity': 'O(V) - stores nodes in priority queue'
            },
            'Bidirectional BFS': {
                'name': 'Bidirectional Breadth-First Search',
                'description': 'Searches from both start and end simultaneously.',
                'how_it_works': [
                    '1. Starts BFS from both start and end',
                    '2. Explores from both directions',
                    '3. Stops when searches meet in middle',
                    '4. Combines paths from both sides'
                ],
                'guarantees': 'Always finds the SHORTEST path',
                'best_for': 'Large mazes where meeting point is known',
                'time_complexity': 'O(V + E) - often faster than unidirectional',
                'space_complexity': 'O(V) - stores nodes from both searches'
            },
            'Uniform Cost Search': {
                'name': 'Uniform Cost Search',
                'description': 'Explores nodes in order of their costs from start.',
                'how_it_works': [
                    '1. Assigns cost 0 to start node',
                    '2. Always explores lowest cost unvisited node',
                    '3. Updates costs to neighbors',
                    '4. Continues until goal reached'
                ],
                'guarantees': 'Finds LOWEST cost path (optimal)',
                'best_for': 'Graphs with varying edge costs',
                'time_complexity': 'O((V + E) log V) with priority queue',
                'space_complexity': 'O(V) - stores all nodes with costs'
            },
            'Jump Point Search': {
                'name': 'Jump Point Search',
                'description': 'Optimized grid pathfinding that skips redundant nodes.',
                'how_it_works': [
                    '1. Identifies key points (jump points) in grid',
                    '2. Only considers nodes that change direction',
                    '3. Skips straight-line nodes',
                    '4. Reduces nodes to explore significantly'
                ],
                'guarantees': 'Finds SHORTEST path in grids',
                'best_for': 'Large grid-based mazes',
                'time_complexity': 'O(V) but with much smaller constant',
                'space_complexity': 'O(V) - but explores fewer nodes'
            }
        }

        exp = explanations.get(algo, {})

        print("\n" + "="*70)
        print(f"  {exp.get('name', algo)}")
        print("="*70)
        print(f"\n📝 DESCRIPTION:")
        print(f"   {exp.get('description', '')}")
        print(f"\n🔧 HOW IT WORKS:")
        for step in exp.get('how_it_works', []):
            print(f"   {step}")
        print(f"\n✅ GUARANTEE:")
        print(f"   {exp.get('guarantees', '')}")
        print(f"\n🎯 BEST FOR:")
        print(f"   {exp.get('best_for', '')}")
        print(f"\n📊 COMPLEXITY:")
        print(f"   Time: {exp.get('time_complexity', '')}")
        print(f"   Space: {exp.get('space_complexity', '')}")
        print(f"\n📈 PERFORMANCE IN THIS MAZE:")
        print(f"   Nodes Explored: {result['nodes_explored']}")
        print(f"   Path Length: {result['path_length']}")
        print(f"   Time Taken: {result['time']*1000:.2f} ms")
        print("="*70 + "\n")
