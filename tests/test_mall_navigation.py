import pytest
from src.mall_navigation import MallMap

def test_mall_map_basic_path():
    """
    Test finding a path between two directly connected stores
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    
    path = mall.find_shortest_path("Apple Store", "Nike")
    assert path == ["Apple Store", "Nike"]

def test_mall_map_multi_step_path():
    """
    Test finding a path that requires multiple steps
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    mall.add_connection("Nike", "Starbucks", 30)
    mall.add_connection("Apple Store", "Starbucks", 100)
    
    path = mall.find_shortest_path("Apple Store", "Starbucks")
    assert path == ["Apple Store", "Nike", "Starbucks"]

def test_mall_map_same_store():
    """
    Test path from a store to itself
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    
    path = mall.find_shortest_path("Apple Store", "Apple Store")
    assert path == ["Apple Store"]

def test_mall_map_no_path():
    """
    Test finding a path between unconnected stores
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    
    path = mall.find_shortest_path("Apple Store", "Starbucks")
    assert path is None

def test_mall_map_negative_distance():
    """
    Test adding a connection with negative distance
    """
    mall = MallMap()
    with pytest.raises(ValueError, match="Distance cannot be negative"):
        mall.add_connection("Apple Store", "Nike", -50)

def test_mall_map_nonexistent_store():
    """
    Test finding path with nonexistent start or end store
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    
    with pytest.raises(KeyError, match="Start store"):
        mall.find_shortest_path("Starbucks", "Nike")
    
    with pytest.raises(KeyError, match="End store"):
        mall.find_shortest_path("Apple Store", "Starbucks")

def test_mall_map_complex_path():
    """
    Test finding path in a more complex mall layout
    """
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike", 50)
    mall.add_connection("Nike", "Starbucks", 30)
    mall.add_connection("Apple Store", "H&M", 40)
    mall.add_connection("H&M", "Starbucks", 60)
    
    path = mall.find_shortest_path("Apple Store", "Starbucks")
    assert path == ["Apple Store", "Nike", "Starbucks"]