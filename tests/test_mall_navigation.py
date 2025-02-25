import pytest
from src.mall_navigation import find_shortest_path

def test_direct_path_between_stores():
    mall_map = {
        'Apple Store': {'Samsung Store': 5},
        'Samsung Store': {'Apple Store': 5}
    }
    path, distance = find_shortest_path(mall_map, 'Apple Store', 'Samsung Store')
    assert path == ['Apple Store', 'Samsung Store']
    assert distance == 5

def test_multi_hop_path():
    mall_map = {
        'Apple Store': {'Samsung Store': 10, 'Microsoft Store': 5},
        'Samsung Store': {'Apple Store': 10, 'Microsoft Store': 3},
        'Microsoft Store': {'Apple Store': 5, 'Samsung Store': 3}
    }
    path, distance = find_shortest_path(mall_map, 'Apple Store', 'Samsung Store')
    assert path == ['Apple Store', 'Microsoft Store', 'Samsung Store']
    assert distance == 8

def test_same_store_path():
    mall_map = {
        'Apple Store': {'Samsung Store': 5},
        'Samsung Store': {'Apple Store': 5}
    }
    path, distance = find_shortest_path(mall_map, 'Apple Store', 'Apple Store')
    assert path == ['Apple Store']
    assert distance == 0

def test_invalid_store_raises_error():
    mall_map = {
        'Apple Store': {'Samsung Store': 5},
        'Samsung Store': {'Apple Store': 5}
    }
    with pytest.raises(ValueError, match="Start or end store not found in mall map"):
        find_shortest_path(mall_map, 'Apple Store', 'Unknown Store')
    
    with pytest.raises(ValueError, match="Start or end store not found in mall map"):
        find_shortest_path(mall_map, 'Unknown Store', 'Samsung Store')

def test_complex_mall_navigation():
    mall_map = {
        'Apple Store': {'Samsung Store': 10, 'Microsoft Store': 5, 'Dell Store': 15},
        'Samsung Store': {'Apple Store': 10, 'Microsoft Store': 3, 'Dell Store': 8},
        'Microsoft Store': {'Apple Store': 5, 'Samsung Store': 3, 'Dell Store': 12},
        'Dell Store': {'Apple Store': 15, 'Samsung Store': 8, 'Microsoft Store': 12}
    }
    path, distance = find_shortest_path(mall_map, 'Apple Store', 'Dell Store')
    assert path == ['Apple Store', 'Microsoft Store', 'Samsung Store', 'Dell Store']
    assert distance == 16

def test_disconnected_stores():
    mall_map = {
        'Apple Store': {'Samsung Store': 5},
        'Samsung Store': {'Apple Store': 5},
        'Microsoft Store': {}
    }
    result = find_shortest_path(mall_map, 'Apple Store', 'Microsoft Store')
    assert result is None