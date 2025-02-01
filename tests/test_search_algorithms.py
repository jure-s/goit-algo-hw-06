import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from task_2_search_algorithms import dfs_path, bfs_path
from task_1_graph_model import create_transport_network

class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        """Ініціалізація графа перед кожним тестом"""
        self.G = create_transport_network()

    def test_dfs_path(self):
        """Перевірка правильності роботи алгоритму DFS"""
        self.assertEqual(dfs_path(self.G, "A", "F"), ['A', 'B', 'E', 'F'])

    def test_bfs_path(self):
        """Перевірка правильності роботи алгоритму BFS"""
        self.assertEqual(bfs_path(self.G, "A", "F"), ['A', 'D', 'F'])

    def test_no_path(self):
        """Перевірка поведінки при відсутності шляху"""
        self.G.remove_edge("E", "F")  # Видаляємо критичне ребро
        self.G.remove_edge("C", "D")  # Видаляємо ще одне критичне ребро
        self.G.remove_edge("A", "D")  # Видаляємо ще одне критичне ребро
        self.G.remove_node("F")       # Видаляємо ізольовану вершину
        print("Граф після видалення ребер:", self.G.edges())
        print("DFS шлях після видалення:", dfs_path(self.G, "A", "F"))
        print("BFS шлях після видалення:", bfs_path(self.G, "A", "F"))
        self.assertIsNone(dfs_path(self.G, "A", "F"))
        self.assertIsNone(bfs_path(self.G, "A", "F"))

if __name__ == "__main__":
    unittest.main()
