#A* Search Algorithm
from queue import PriorityQueue

def a_star_search(graph, start, goal, h):
    """
    Perform A* Search on a graph.
    
    Parameters:
    - graph: dict, adjacency list with edge costs (e.g., {'A': {'B': 1, 'C': 3}, ...})
    - start: starting node
    - goal: goal node
    - h: dict, heuristic values for each node
    
    Returns:
    - path: list, representing the path from start to goal if found, else None
    """
    open_list = PriorityQueue()
    open_list.put((0, [start]))
    g_costs = {start: 0}

    while not open_list.empty():
        cost, path = open_list.get()
        current = path[-1]

        if current == goal:
            return path

        for neighbor, weight in graph.get(current, {}).items():
            g_cost = g_costs[current] + weight
            f_cost = g_cost + h.get(neighbor, float('inf'))

            if neighbor not in g_costs or g_cost < g_costs[neighbor]:
                g_costs[neighbor] = g_cost
                new_path = path + [neighbor]
                open_list.put((f_cost, new_path))

    return None

# Example graph and heuristic
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}
heuristic = {'A': 6, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 0}

# Perform A* Search
start_node = 'A'
goal_node = 'F'
path = a_star_search(graph, start_node, goal_node, heuristic)

# Display the results
if path:
    print(f"A* Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
