import pytest
from src.mall_navigation import MallMap

def test_add_store():
    """Test adding a store to the mall map."""
    mall = MallMap()
    mall.add_store("Apple Store")
    assert "Apple Store" in mall.graph
    
    # Test adding a duplicate store raises an error
    with pytest.raises(ValueError, match="Store Apple Store already exists"):
        mall.add_store("Apple Store")

def test_add_connection():
    """Test adding connections between stores."""
    mall = MallMap()
    
    # Prepare stores
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    
    # Add valid connection
    mall.add_connection("Apple Store", "Nike Store", 10)
    
    # Check bidirectional connection
    assert mall.graph["Apple Store"]["Nike Store"] == 10
    assert mall.graph["Nike Store"]["Apple Store"] == 10
    
    # Test invalid connections
    with pytest.raises(ValueError, match="does not exist in the mall map"):
        mall.add_connection("Apple Store", "Nonexistent Store", 5)
    
    with pytest.raises(ValueError, match="cannot be negative"):
        mall.add_connection("Apple Store", "Nike Store", -5)

def test_find_shortest_path():
    """Test finding the shortest path between stores."""
    mall = MallMap()
    
    # Create a mall map with multiple stores and connections
    stores = ["Apple Store", "Nike Store", "Starbucks", "Bookstore", "Electronics Store"]
    for store in stores:
        mall.add_store(store)
    
    # Add connections
    mall.add_connection("Apple Store", "Nike Store", 10)
    mall.add_connection("Nike Store", "Starbucks", 15)
    mall.add_connection("Apple Store", "Starbucks", 30)
    mall.add_connection("Apple Store", "Bookstore", 5)
    mall.add_connection("Bookstore", "Starbucks", 10)
    
    # Test direct path
    assert mall.find_shortest_path("Apple Store", "Nike Store") == ["Apple Store", "Nike Store"]
    
    # Test multi-hop shortest path
    assert mall.find_shortest_path("Apple Store", "Starbucks") == ["Apple Store", "Bookstore", "Starbucks"]
    
    # Test same store path
    assert mall.find_shortest_path("Apple Store", "Apple Store") == ["Apple Store"]

def test_path_finding_errors():
    """Test error cases in path finding."""
    mall = MallMap()
    mall.add_store("Apple Store")
    
    # Test finding path with nonexistent stores
    with pytest.raises(ValueError, match="does not exist in the mall map"):
        mall.find_shortest_path("Apple Store", "Nonexistent Store")
    
    with pytest.raises(ValueError, match="does not exist in the mall map"):
        mall.find_shortest_path("Nonexistent Store", "Apple Store")

def test_no_path_exists():
    """Test scenario where no path exists between stores."""
    mall = MallMap()
    
    # Create isolated stores
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    
    # No connection between stores
    assert mall.find_shortest_path("Apple Store", "Nike Store") is None