import networkx as nx
import matplotlib.pyplot as plt

def create_transport_network():
    # Створення графа, що моделює транспортну мережу міста
    G = nx.Graph()
    
    # Додавання вершин (станції або перехрестя)
    G.add_nodes_from([
        ("A", {"location": "Центр"}),
        ("B", {"location": "Північ"}),
        ("C", {"location": "Південь"}),
        ("D", {"location": "Захід"}),
        ("E", {"location": "Схід"}),
        ("F", {"location": "Передмістя"})
    ])
    
    # Додавання ребер (дороги між місцями)
    G.add_edges_from([
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("A", "E"),
        ("B", "E"),
        ("C", "D"),
        ("D", "F"),
        ("E", "F")
    ])
    
    return G

def create_weighted_transport_network():
    # Створення графа з вагами, що представляє транспортну мережу
    G = nx.Graph()
    
    # Додавання вершин (станції або перехрестя)
    G.add_nodes_from([
        ("A", {"location": "Центр"}),
        ("B", {"location": "Північ"}),
        ("C", {"location": "Південь"}),
        ("D", {"location": "Захід"}),
        ("E", {"location": "Схід"}),
        ("F", {"location": "Передмістя"})
    ])
    
    # Додавання ребер з вагами (відстань у км)
    G.add_weighted_edges_from([
        ("A", "B", 4),
        ("A", "C", 2),
        ("A", "D", 5),
        ("A", "E", 1),
        ("B", "E", 3),
        ("C", "D", 8),
        ("D", "F", 6),
        ("E", "F", 7)
    ])
    
    return G

def analyze_graph(G):
    # Аналіз характеристик графа
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())
    
    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print(f"Ступінь вершин: {degrees}")

def visualize_graph(G):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Розташування вершин
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Транспортна мережа міста")
    plt.show()

if __name__ == "__main__":
    G = create_transport_network()
    analyze_graph(G)
    visualize_graph(G)

    GW = create_weighted_transport_network()
    analyze_graph(GW)
    visualize_graph(GW)
