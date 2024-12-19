import unittest
from dinics_algorithm import DinicsAlgorithm

class TestMaxFlow(unittest.TestCase):
    
    def test_simple_network(self):
        node_count = 4
        source, sink = 0, 3
        irrigation = DinicsAlgorithm(node_count)
        
        irrigation.add_edge(0, 1, 10)
        irrigation.add_edge(1, 3, 10)
        
        max_flow = irrigation.max_flow(source, sink)
        self.assertEqual(max_flow, 10)
        
    def test_multiple_paths(self):
        node_count = 5
        source, sink = 0, 4
        irrigation = DinicsAlgorithm(node_count)
        
        irrigation.add_edge(0, 1, 10)
        irrigation.add_edge(0, 2, 5)
        irrigation.add_edge(1, 3, 15)
        irrigation.add_edge(2, 3, 10)
        irrigation.add_edge(3, 4, 10)
        
        max_flow = irrigation.max_flow(source, sink)
        self.assertEqual(max_flow, 15)
        
    def test_disconnected_network(self):
        node_count = 3
        source, sink = 0, 2
        irrigation = DinicsAlgorithm(node_count)
        
        irrigation.add_edge(0, 1, 10)
        irrigation.add_edge(1, 1, 5)
        
        max_flow = irrigation.max_flow(source, sink)
        self.assertEqual(max_flow, 0)
        
    def test_zero_capacity_edges(self):
        node_count = 3
        source, sink = 0, 2
        irrigation = DinicsAlgorithm(node_count)
        
        irrigation.add_edge(0, 1, 0)
        irrigation.add_edge(1, 2, 10)
        
        max_flow = irrigation.max_flow(source, sink)
        self.assertEqual(max_flow, 0)
