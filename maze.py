from maze.maze_generator import MazeGenerator
from algorithms import BFS, DFS, Dijkstra, AStar, GreedyBestFirst, BidirectionalBFS, UniformCostSearch, JumpPointSearch
from visualizer import AnimatedMazeVisualizer
from comparison import compare_all_algorithms
from menu import show_menu


# Main program
if __name__ == "__main__":
    maze_gen = None

    while True:
        if maze_gen is None:
            print("\n🎲 Generating new maze...")
            maze_gen = MazeGenerator(width=15, height=15, loop_factor=0.2)
            maze_gen.generate()
            maze_gen.add_entrance_exit()
            print("✅ Maze generated with multiple paths!")

        choice = show_menu()

        if choice == '0':
            print("\n👋 Thanks for using the Maze Solver! Goodbye!\n")
            break

        elif choice == '10':
            maze_gen = None
            continue

        elif choice == '9':
            compare_all_algorithms(
                maze_gen.maze, maze_gen.start, maze_gen.end, save_charts=True)

        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            visualizer = AnimatedMazeVisualizer(
                maze_gen.maze, maze_gen.start, maze_gen.end)

            print("\n🚀 Starting algorithm visualization...\n")

            if choice == '1':
                solver = BFS(maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '2':
                solver = DFS(maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '3':
                solver = Dijkstra(maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '4':
                solver = AStar(maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '5':
                solver = GreedyBestFirst(
                    maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '6':
                solver = BidirectionalBFS(
                    maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '7':
                solver = UniformCostSearch(
                    maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()
            elif choice == '8':
                solver = JumpPointSearch(
                    maze_gen.maze, maze_gen.start, maze_gen.end)
                result = solver.solve_with_steps()

            if result:
                visualizer.animate_solution(result)
            else:
                print("❌ No solution found!")

        else:
            print("\n⚠️  Invalid choice! Please enter 0-10.")

        input("\nPress Enter to continue...")
