# 🧩 Maze Solver Visualizer

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Algorithms](https://img.shields.io/badge/Algorithms-DFS%20%7C%20BFS%20%7C%20A*%20%7C%20Dijkstra-success)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)

A **maze generation and maze solving visualizer** built using Python.  
This project demonstrates how different **pathfinding algorithms** work by visually solving the same maze and comparing their behavior, performance, and efficiency.

> 🎯 Designed for **learning algorithms, visualization, and portfolio demonstration**

---

## 🚀 Features

- 🧱 Random maze generation
- 🧠 Multiple maze-solving algorithms
- 🎥 Step-by-step visualization
- 📊 Algorithm performance comparison
- 🔄 Reusable and modular code structure

---

🧠 Algorithms Implemented

| Algorithm                      | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| **A***                         | Heuristic-based optimal pathfinding using cost + estimated distance          |
| **Breadth-First Search (BFS)** | Explores level by level and guarantees the shortest path in unweighted mazes |
| **Bidirectional BFS**          | Runs BFS simultaneously from start and goal to reduce search space           |
| **Depth-First Search (DFS)**   | Explores deeply along paths; fast but not guaranteed optimal                 |
| **Dijkstra’s Algorithm**       | Guarantees shortest path by exploring lowest-cost nodes first                |
| **Greedy Best-First Search**   | Uses heuristic only; fast but may produce suboptimal paths                   |
| **Jump Point Search (JPS)**    | Optimized A* variant for grid-based mazes, skips unnecessary nodes           |
| **Uniform Cost Search (UCS)**  | Expands nodes based on path cost; equivalent to Dijkstra without heuristics  |

---

## 🖼️ Visual Demo

<img width="719" height="507" alt="image" src="https://github.com/user-attachments/assets/feb9f272-998c-46db-9e59-a7578ddc82df" />


<img width="1214" height="672" alt="image" src="https://github.com/user-attachments/assets/24031524-637d-43b3-aadc-356b12b6ff3d" />



---

## 🛠️ Tech Stack

- **Language:** Python 🐍
- **Visualization:** Pygame / Matplotlib *(depending on your implementation)*
- **Concepts Used:**
  - Graph traversal
  - Heuristics
  - Data structures (Stack, Queue, Priority Queue)

---

## 📂 Project Structure
```
3D-Maze-Solver/
│
├── algorithms/                 # Pathfinding algorithms
│   ├── astar.py
│   ├── bfs.py
│   ├── bidirectional_bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   ├── greedy_bfs.py
│   ├── jump_point_search.py
│   ├── uniform_cost_search.py
│   └── base_solver.py          # Common solver interface
│
├── charts/                     
│   └── algorithm_comparison.png   # Performance charts & comparisons
│
├── maze/                       # Maze generation & logic
│   ├── maze.py                 # Core maze data structure
│   ├── maze_generator.py       # Maze generation logic
│   └── comparison.py           # Algorithm comparison logic
│
├── visualizer.py               # Maze & algorithm visualization
├── menu.py                     # Algorithm selection menu / UI
├── maze.py                     # 🚀 ENTRY POINT (main execution file)
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/UsmanDanial04/Algorithm-Analysis.git
cd Algorithm-Analysis
```

## 🎯 Learning Outcomes

- Deep understanding of pathfinding algorithms
- Hands-on experience with visual simulations
- Clean and modular Python architecture
- Strong portfolio-level project for GitHub & LinkedIn


## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.


## 👤 Author

### Usman Danial
📌 Aspiring Software Engineer | Python Developer | AI & Visualization Enthusiast

🔗 LinkedIn: www.linkedin.com/in/usman-danial-b4568b289 

⭐ If you like this project, don’t forget to star the repo!
