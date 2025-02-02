import heapq
from task_1_graph_model import create_weighted_transport_network

def dijkstra_shortest_path(graph, start, goal):
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху в зваженому графі.
    """
    priority_queue = [(0, start, [])]  # Кортежі: (відстань, поточна вершина, шлях)
    visited = set()
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    
    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        path = path + [current_node]
        
        if current_node == goal:
            return path, current_distance
        
        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, path))
    
    return None, float('inf')

def main():
    G = create_weighted_transport_network()
    start, goal = "A", "F"
    path, distance = dijkstra_shortest_path(G, start, goal)
    print(f"Найкоротший шлях з {start} до {goal}: {path} з відстанню {distance}")

if __name__ == "__main__":
    main()
