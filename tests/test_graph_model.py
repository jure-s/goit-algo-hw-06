import unittest
from src.task_1_graph_model import create_transport_network

class TestGraphModel(unittest.TestCase):

    def test_graph_structure(self):
        G = create_transport_network()
        self.assertEqual(G.number_of_nodes(), 6)
        self.assertEqual(G.number_of_edges(), 8)
        self.assertTrue(G.has_edge("A", "B"))
        self.assertTrue(G.has_node("F"))

    def test_node_attributes(self):
        G = create_transport_network()
        self.assertEqual(G.nodes["A"]["location"], "Центр")

if __name__ == "__main__":
    unittest.main()
