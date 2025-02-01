import sys
import os
import unittest

# Додаємо шлях до кореневої папки проєкту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from task_3_dijkstra_algorithm import dijkstra_shortest_path
from task_1_graph_model import create_weighted_transport_network

class TestDijkstraAlgorithm(unittest.TestCase):

    def setUp(self):
        """Ініціалізація графа перед кожним тестом"""
        self.G = create_weighted_transport_network()

    def test_shortest_path(self):
        """Перевірка знаходження найкоротшого шляху між двома вершинами"""
        path, distance = dijkstra_shortest_path(self.G, "A", "F")
        self.assertEqual(path, ['A', 'E', 'F'])
        self.assertEqual(distance, 8)

    def test_no_path(self):
        """Перевірка поведінки при відсутності шляху"""
        self.G.remove_edge("E", "F")  # Видаляємо критичне ребро
        self.G.remove_edge("D", "F")  # Видаляємо ще одне критичне ребро
        path, distance = dijkstra_shortest_path(self.G, "A", "F")
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))

if __name__ == "__main__":
    unittest.main()
