#Greedy Best-First Search Algorithm
from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, h):
    """
    Perform Greedy Best-First Search on a graph.
    
    Parameters:
    - graph: dict, adjacency list representation of the graph
    - start: starting node
    - goal: goal node
    - h: dict, heuristic values for each node
    
    Returns:
    - path: list, representing the path from start to goal if found, else None
    """
    open_list = PriorityQueue()
    open_list.put((h[start], [start]))
    visited = set()

    while not open_list.empty():
        heuristic, path = open_list.get()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, {}):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    open_list.put((h.get(neighbor, float('inf')), new_path))

    return None

# Example graph and heuristic
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {'A': 6, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 0}

# Perform Greedy Best-First Search
start_node = 'A'
goal_node = 'F'
path = greedy_best_first_search(graph, start_node, goal_node, heuristic)

# Display the results
if path:
    print(f"Greedy Best-First Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
