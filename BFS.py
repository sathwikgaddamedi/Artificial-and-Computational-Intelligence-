#BreadthFirst search Algorithm implementation 
from collections import deque

def bfs(graph, start_node, goal_node):
    """
    Perform Breadth-First Search on a graph.
    
    Parameters:
    - graph: dict, adjacency list representation of the graph
    - start_node: starting node for the search
    - goal_node: node to search for
    
    Returns:
    - path: list, representing the path from start_node to goal_node if found, else None
    """
    # Initialize the queue with the start node and the visited set
    queue = deque([[start_node]])
    visited = set()

    while queue:
        # Dequeue the first path from the queue
        path = queue.popleft()
        node = path[-1]

        # Check if we have reached the goal node
        if node == goal_node:
            return path

        # Skip nodes that have already been visited
        if node not in visited:
            visited.add(node)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # If the queue is empty and no path was found
    return None

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Input: Start and Goal nodes
start_node = 'A'
goal_node = 'F'

# Perform BFS
path = bfs(graph, start_node, goal_node)

# Display the results
if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
