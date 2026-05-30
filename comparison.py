import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import os
from algorithms import BFS, DFS, Dijkstra, AStar, GreedyBestFirst, BidirectionalBFS, UniformCostSearch, JumpPointSearch


def compare_all_algorithms(maze, start, end, save_charts=False):
    """Run and compare all algorithms"""
    print("\n🔄 Running all algorithms...")

    algorithms = [
        ('BFS', BFS(maze, start, end).solve_with_steps),
        ('DFS', DFS(maze, start, end).solve_with_steps),
        ('Dijkstra', Dijkstra(maze, start, end).solve_with_steps),
        ('A*', AStar(maze, start, end).solve_with_steps),
        ('Greedy Best-First', GreedyBestFirst(maze, start, end).solve_with_steps),
        ('Bidirectional BFS', BidirectionalBFS(maze, start, end).solve_with_steps),
        ('Uniform Cost Search', UniformCostSearch(
            maze, start, end).solve_with_steps),
        ('Jump Point Search', JumpPointSearch(maze, start, end).solve_with_steps)
    ]

    results = []
    for name, func in algorithms:
        print(f"  Running {name}...")
        result = func()
        if result:
            results.append(result)

    # Create comparison visualization
    fig, axes = plt.subplots(2, 4, figsize=(24, 12))
    axes = axes.flatten()

    grass_color = '#2d5016'
    path_color = '#ffffff'
    colors = [path_color, grass_color]
    cmap = LinearSegmentedColormap.from_list('maze', colors, N=2)

    colors_map = {'BFS': '#2196F3', 'DFS': '#4CAF50', 'Dijkstra': '#FF9800', 'A*': '#E91E63',
                  'Greedy Best-First': '#9C27B0', 'Bidirectional BFS': '#00BCD4',
                  'Uniform Cost Search': '#795548', 'Jump Point Search': '#607D8B'}

    for idx, result in enumerate(results):
        ax = axes[idx]
        ax.imshow(maze, cmap=cmap, interpolation='nearest')

        # Draw final path
        if result['path']:
            path = result['path']
            path_y = [p[0] for p in path]
            path_x = [p[1] for p in path]
            ax.plot(path_x, path_y, color=colors_map[result['algorithm']],
                    linewidth=3, alpha=0.8)

        # Markers
        start_circle = patches.Circle((start[1], start[0]),
                                      radius=0.5, color='lime', zorder=10)
        ax.add_patch(start_circle)

        end_circle = patches.Circle((end[1], end[0]),
                                    radius=0.5, color='red', zorder=10)
        ax.add_patch(end_circle)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{result['algorithm']}\nNodes: {result['nodes_explored']} | "
                     f"Path: {result['path_length']} | Time: {result['time']*1000:.2f}ms",
                     fontsize=10, fontweight='bold')

    plt.suptitle('Algorithm Comparison (8 Algorithms)',
                 fontsize=16, fontweight='bold')
    plt.tight_layout()

    if save_charts:
        chart_path = os.path.join('charts', 'algorithm_comparison.png')
        plt.savefig(chart_path)
        print(f"Comparison chart saved to {chart_path}")

    plt.show()

    # Print comparison
    print("\n" + "="*100)
    print("  ALGORITHM COMPARISON RESULTS")
    print("="*100)
    print(f"\n{'Algorithm':<25} {'Nodes':<10} {'Path Length':<15} {'Time (ms)':<12}")
    print("-"*100)
    for r in results:
        print(
            f"{r['algorithm']:<25} {r['nodes_explored']:<10} {r['path_length']:<15} {r['time']*1000:<12.3f}")
    print("="*100)

    # Save comparison data if requested
    if save_charts:
        import json
        data_path = os.path.join('charts', 'comparison_data.json')

        # Create a summary without non-serializable data (sets)
        summary_results = []
        for result in results:
            summary = {
                'algorithm': result['algorithm'],
                'nodes_explored': result['nodes_explored'],
                'path_length': result['path_length'],
                'time': result['time'],
                'path': result['path']  # This is a list, so it's serializable
            }
            summary_results.append(summary)

        with open(data_path, 'w') as f:
            json.dump(summary_results, f, indent=2)
        print(f"Comparison data saved to {data_path}")
