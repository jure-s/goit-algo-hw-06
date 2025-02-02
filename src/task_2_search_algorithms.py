import networkx as nx
from task_1_graph_model import create_transport_network

def dfs_path(graph, start, goal):
    """
    Реалізація пошуку в глибину (DFS) для знаходження шляху від start до goal.
    """
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(list(graph.neighbors(node))):  # Додаємо у зворотному порядку для коректного порядку обходу
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start, goal):
    """
    Реалізація пошуку в ширину (BFS) для знаходження шляху від start до goal.
    """
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

def compare_search_algorithms(graph, start, goal):
    dfs_result = dfs_path(graph, start, goal)
    bfs_result = bfs_path(graph, start, goal)
    
    print(f"DFS шлях з {start} до {goal}: {dfs_result}")
    print(f"BFS шлях з {start} до {goal}: {bfs_result}")
    
    if dfs_result == bfs_result:
        print("Обидва алгоритми знайшли однаковий шлях.")
    else:
        print("Різниця між DFS і BFS:")
        print("- DFS досліджує шлях максимально глибоко перед поверненням назад, тому шлях може бути довшим.")
        print("- BFS перевіряє всі можливі маршрути рівня за рівнем, гарантуючи найкоротший шлях у кількості кроків.")

def main():
    G = create_transport_network()
    start, goal = "A", "F"
    compare_search_algorithms(G, start, goal)

if __name__ == "__main__":
    main()
