import pytest
from src.knapsack_solver import knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    max_weight = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    assert knapsack(max_weight, weights, values) == 220

def test_knapsack_cannot_fit_all():
    """Test scenario where not all items can be included"""
    max_weight = 20
    weights = [10, 20, 30]
    values = [60, 100, 120]
    assert knapsack(max_weight, weights, values) == 160

def test_knapsack_zero_weight():
    """Test scenario with zero weight capacity"""
    max_weight = 0
    weights = [10, 20, 30]
    values = [60, 100, 120]
    assert knapsack(max_weight, weights, values) == 0

def test_knapsack_empty_input():
    """Test scenario with empty inputs"""
    max_weight = 50
    weights = []
    values = []
    assert knapsack(max_weight, weights, values) == 0

def test_mismatched_input_lengths():
    """Test error handling for mismatched input lengths"""
    max_weight = 50
    weights = [10, 20]
    values = [60, 100, 120]
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        knapsack(max_weight, weights, values)