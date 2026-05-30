def show_menu():
    """Display algorithm selection menu"""
    print("\n" + "="*70)
    print("  🎮 MAZE SOLVING ALGORITHM SELECTOR")
    print("="*70)
    print("\n  Select an algorithm to watch it solve the maze:\n")
    print("  1. BFS (Breadth-First Search) - Explores level by level")
    print("  2. DFS (Depth-First Search) - Explores deep first")
    print("  3. Dijkstra's Algorithm - Shortest path with costs")
    print("  4. A* (A-Star) - Smart heuristic search")
    print("  5. Greedy Best-First - Fast but not optimal")
    print("  6. Bidirectional BFS - Searches from both ends")
    print("  7. Uniform Cost Search - Cost-based exploration")
    print("  8. Jump Point Search - Optimized grid search")
    print("  9. Compare All Algorithms")
    print(" 10. Generate New Maze")
    print("  0. Exit")
    print("\n" + "="*70)

    choice = input("\n  Enter your choice (0-10): ").strip()
    return choice
