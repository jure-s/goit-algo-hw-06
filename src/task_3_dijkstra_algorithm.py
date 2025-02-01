import sys
import os
import networkx as nx
from task_1_graph_model import create_weighted_transport_network

def dijkstra_shortest_path(graph, start, goal):
    """
    Використання алгоритму Дейкстри для знаходження найкоротшого шляху.
    """
    try:
        path = nx.dijkstra_path(graph, source=start, target=goal, weight='weight')
        distance = nx.dijkstra_path_length(graph, source=start, target=goal, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, float('inf')

if __name__ == "__main__":
    # Додаємо шлях до кореневого каталогу для коректного імпорту
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    G = create_weighted_transport_network()
    start_node = "A"
    goal_node = "F"

    path, distance = dijkstra_shortest_path(G, start_node, goal_node)
    print(f"Найкоротший шлях з {start_node} до {goal_node}: {path} з відстанню {distance}")
