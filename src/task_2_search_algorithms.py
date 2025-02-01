import networkx as nx
from task_1_graph_model import create_transport_network

def dfs_path(graph, start, goal):
    """
    Пошук у глибину (DFS) для знаходження шляху від start до goal.
    """
    if start not in graph or goal not in graph:
        return None

    try:
        predecessors = nx.dfs_predecessors(graph, source=start)
        if goal not in predecessors:
            return None
        
        path = [goal]
        while path[-1] in predecessors:
            path.append(predecessors[path[-1]])
        path.reverse()
        return path
    except KeyError:
        return None

def bfs_path(graph, start, goal):
    """
    Пошук у ширину (BFS) для знаходження шляху від start до goal.
    """
    if start not in graph or goal not in graph:
        return None

    try:
        path = list(nx.shortest_path(graph, source=start, target=goal))
        return path
    except nx.NetworkXNoPath:
        return None
    except nx.NodeNotFound:
        return None

def compare_search_algorithms(graph, start, goal):
    dfs_result = dfs_path(graph, start, goal)
    bfs_result = bfs_path(graph, start, goal)
    
    print(f"DFS шлях з {start} до {goal}: {dfs_result}")
    print(f"BFS шлях з {start} до {goal}: {bfs_result}")
    
    if dfs_result == bfs_result:
        print("Шляхи збігаються.")
    else:
        print("Шляхи відрізняються через особливості алгоритмів.")

if __name__ == "__main__":
    G = create_transport_network()
    start_node = "A"
    goal_node = "F"
    compare_search_algorithms(G, start_node, goal_node)