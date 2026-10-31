# Artificial Intelligence – Programming Assignment No. 1

## Romania Map Search Algorithms

**Course:** Artificial Intelligence  
**Semester:** Fall 2026  
**Assignment:** Programming Assignment No. 1  
**Language:** Python

## 1. Project Overview

This project implements four Artificial Intelligence search algorithms using the classic Romania Map problem.

The program finds a route between a user-selected source city and destination city. It calculates the total path distance for each algorithm and compares their results in ascending order of path cost.

The program supports different source and destination combinations, allowing users to explore how different search algorithms find routes.

## 2. Algorithms Implemented

The following four search algorithms are implemented:

### 1. Breadth First Search (BFS)
- Explores cities level by level.
- Uses a FIFO queue.
- Finds a path with the minimum number of edges.

### 2. Uniform Cost Search (UCS)
- Expands the path with the lowest accumulated cost.
- Uses a priority queue.
- Finds the least-cost path when edge costs are non-negative.

### 3. Greedy Best First Search (GBFS)
- Uses heuristic values to guide the search.
- Selects the next city based on its estimated distance to the destination.
- Prioritizes estimated closeness to the goal.

### 4. Iterative Deepening Depth First Search (IDDFS)
- Combines the depth-first search approach with repeated depth limits.
- Increases the search depth gradually.
- Searches until the destination is found.

## 3. Features

- Interactive source city selection.
- Interactive destination city selection.
- Romania road map with city connections and distances.
- Heuristic-based search.
- Automatic execution of all four algorithms.
- Complete route/path display.
- Total distance calculation in kilometres.
- Comparison of algorithm results.
- Ranking of paths in ascending order of total cost.

## 4. Technologies Used

- Python 3
- Collections Module
- Heapq Module

No external Python libraries are required.

## 5. Project Structure

```text
AI-Assignment-1/
│
├── AI_Assignment_1.py
│
└── README.md
```

## 6. How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Open the project directory.

```bash
cd AI-Assignment-1
```

**Step 3:** Run the Python program.

```bash
python AI_Assignment_1.py
```

**Step 4:** Enter your desired source and destination cities when prompted.

The program will execute all four search algorithms and display their paths, distances, and comparison results.

## 7. Example Input

```text
Enter Source City: Arad
Enter Destination City: Bucharest
```

Other possible test combinations include:

- Timisoara to Bucharest
- Oradea to Craiova
- Iasi to Arad

## 8. Expected Output

The program displays:

- Selected source and destination.
- BFS path and total distance.
- UCS path and total distance.
- Greedy Best First Search path and total distance.
- IDDFS path and total distance.
- Comparison of all algorithms in ascending order of path cost.
- Best result based on minimum path cost.

## 9. Learning Outcomes

Through this assignment, the implementation and comparison of uninformed and informed search strategies were explored.

The project demonstrates how different algorithms search through a graph, use path costs and heuristic information, and produce routes between cities. It also highlights the difference between finding the shortest path in terms of edges and finding the least-cost path in terms of actual distance.

## 10. Author

**Name:** Abdullah Gul  
**Course:** Artificial Intelligence  
**Assignment:** Programming Assignment No. 1  
**Semester:** Fall 2026
