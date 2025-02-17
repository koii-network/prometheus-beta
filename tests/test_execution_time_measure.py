import time
import pytest
from src.execution_time_measure import measure_execution_time

def test_measure_execution_time_basic():
    @measure_execution_time
    def simple_function(x, y):
        return x + y
    
    result, execution_time = simple_function(3, 4)
    
    assert result == 7
    assert execution_time >= 0  # Should always be non-negative

def test_measure_execution_time_with_delay():
    @measure_execution_time
    def delayed_function():
        time.sleep(0.1)
        return "Delayed result"
    
    result, execution_time = delayed_function()
    
    assert result == "Delayed result"
    assert execution_time >= 0.1  # Should take at least 0.1 seconds

def test_measure_execution_time_with_keyword_args():
    @measure_execution_time
    def keyword_function(a=1, b=2):
        return a * b
    
    result, execution_time = keyword_function(a=5, b=3)
    
    assert result == 15
    assert execution_time >= 0

def test_measure_execution_time_complex_function():
    @measure_execution_time
    def complex_function(n):
        return sum(range(n))
    
    result, execution_time = complex_function(10000)
    
    assert result == sum(range(10000))
    assert execution_time >= 0