
# Artificial Intelligence
# Programming Assignment No. 1
# Romania Map Search Algorithms

from collections import deque
import heapq

# Heuristic values (straight-line distance to Bucharest)

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Romania road map with distances

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {
        'Arad': 140, 'Oradea': 151,
        'Fagaras': 99, 'Rimnicu Vilcea': 80
    },
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {
        'Drobeta': 120, 'Rimnicu Vilcea': 146,
        'Pitesti': 138
    },
    'Rimnicu Vilcea': {
        'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97
    },
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {
        'Rimnicu Vilcea': 97, 'Craiova': 138,
        'Bucharest': 101
    },
    'Bucharest': {
        'Fagaras': 211, 'Pitesti': 101,
        'Giurgiu': 90, 'Urziceni': 85
    },
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {
        'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142
    },
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


# Calculate total distance of a path

def path_cost(path):
    total = 0

    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]

    return total


# 1. Breadth First Search

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return path

        for neighbor in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


# 2. Uniform Cost Search

def ucs(start, goal):
    priority_queue = [(0, [start])]
    visited = set()

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        city = path[-1]

        if city == goal:
            return path

        if city in visited:
            continue

        visited.add(city)

        for neighbor, distance in graph[city].items():
            if neighbor not in visited:
                new_cost = cost + distance
                heapq.heappush(
                    priority_queue,
                    (new_cost, path + [neighbor])
                )

    return None


# 3. Greedy Best First Search

def greedy(start, goal):
    priority_queue = [(heuristic[goal] if start == goal else heuristic[start],
                       [start])]
    visited = set()

    while priority_queue:
        _, path = heapq.heappop(priority_queue)
        city = path[-1]

        if city == goal:
            return path

        if city in visited:
            continue

        visited.add(city)

        for neighbor in graph[city]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], path + [neighbor])
                )

    return None


# 4. Iterative Deepening Depth First Search

def depth_limited_search(city, goal, limit, path):

    if city == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph[city]:

        if neighbor not in path:
            result = depth_limited_search(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor]
            )

            if result is not None:
                return result

    return None


def iddfs(start, goal):

    for depth in range(len(graph)):

        result = depth_limited_search(
            start, goal, depth, [start]
        )

        if result is not None:
            return result

    return None


# Display the result of each algorithm

def display_result(name, path):

    if path is None:
        print(name, ": No path found")
        return None

    cost = path_cost(path)

    print("\n", name)
    print("Path:", " -> ".join(path))
    print("Total Distance:", cost, "km")

    return cost


# Main Program

def main():

    cities = sorted(graph.keys())

    print("=" * 55)
    print("       ROMANIA MAP SEARCH ALGORITHMS")
    print("=" * 55)

    print("\nAvailable Cities:")

    for city in cities:
        print(city)

    print("\nSelect Source and Destination")

    start = input("\nEnter Source City: ").strip().title()
    goal = input("Enter Destination City: ").strip().title()

    if start not in graph or goal not in graph:
        print("\nInvalid city name! Please enter a city from the list.")
        return

    print("\nSource:", start)
    print("Destination:", goal)

    print("\n" + "=" * 55)
    print("             ALGORITHM RESULTS")
    print("=" * 55)

    results = []

    # Run BFS
    path = bfs(start, goal)
    cost = display_result("1. Breadth First Search", path)
    if cost is not None:
        results.append(("Breadth First Search", cost, path))

    # Run UCS
    path = ucs(start, goal)
    cost = display_result("2. Uniform Cost Search", path)
    if cost is not None:
        results.append(("Uniform Cost Search", cost, path))

    # Run Greedy
    path = greedy(start, goal)
    cost = display_result("3. Greedy Best First Search", path)
    if cost is not None:
        results.append(("Greedy Best First Search", cost, path))

    # Run IDDFS
    path = iddfs(start, goal)
    cost = display_result("4. Iterative Deepening DFS", path)
    if cost is not None:
        results.append(("Iterative Deepening DFS", cost, path))

    # Compare algorithms in ascending order of path cost

    print("\n" + "=" * 55)
    print("       COMPARISON (LOWEST TO HIGHEST COST)")
    print("=" * 55)

    results.sort(key=lambda x: x[1])

    for rank, (name, cost, path) in enumerate(results, 1):
        print(f"\nRank {rank}: {name}")
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost, "km")

    if results:
        print("\nBest result based on path cost:")
        print(results[0][0])
        print("Minimum Distance:", results[0][1], "km")

    print("\n" + "=" * 55)
    print("             PROGRAM COMPLETED")
    print("=" * 55)


# Start the program

if __name__ == "__main__":
    main()
