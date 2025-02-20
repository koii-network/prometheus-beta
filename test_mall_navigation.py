import unittest
from mall_navigation import MallNavigator

class TestMallNavigation(unittest.TestCase):
    def setUp(self):
        self.mall_map = {
            "entrance": {"electronics_store": 50, "food_court": 30},
            "electronics_store": {"entrance": 50, "clothing_store": 40},
            "clothing_store": {"electronics_store": 40, "food_court": 20},
            "food_court": {"entrance": 30, "clothing_store": 20}
        }
        self.navigator = MallNavigator(self.mall_map)
    
    def test_shortest_path(self):
        path, distance = self.navigator.find_shortest_path("entrance", "clothing_store")
        self.assertEqual(path, ["entrance", "food_court", "clothing_store"])
        self.assertEqual(distance, 50)
    
    def test_same_start_end(self):
        path, distance = self.navigator.find_shortest_path("entrance", "entrance")
        self.assertEqual(path, ["entrance"])
        self.assertEqual(distance, 0)
    
    def test_invalid_store(self):
        with self.assertRaises(ValueError):
            self.navigator.find_shortest_path("entrance", "non_existent_store")
    
    def test_no_direct_path(self):
        # Test a scenario where path exists but not directly
        test_map = {
            "A": {"B": 10},
            "B": {"A": 10, "C": 15},
            "C": {"B": 15}
        }
        nav = MallNavigator(test_map)
        path, distance = nav.find_shortest_path("A", "C")
        self.assertEqual(path, ["A", "B", "C"])
        self.assertEqual(distance, 25)

if __name__ == '__main__':
    unittest.main()