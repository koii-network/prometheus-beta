import pytest
import logging
import psutil
from src.memory_logger import log_memory_usage

class MockLogger:
    def __init__(self):
        self.info_logs = []
    
    def info(self, message):
        self.info_logs.append(message)

def test_log_memory_usage():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Call the function
    memory_stats = log_memory_usage(mock_logger)
    
    # Check return value
    assert isinstance(memory_stats, dict)
    assert 'total' in memory_stats
    assert 'available' in memory_stats
    assert 'used' in memory_stats
    assert 'percent' in memory_stats
    
    # Check logging
    assert len(mock_logger.info_logs) > 0
    
    # Validate memory values
    assert memory_stats['total'] > 0
    assert memory_stats['available'] > 0
    assert memory_stats['used'] > 0
    assert 0 <= memory_stats['percent'] <= 100

def test_default_logger():
    # Test with default logger
    memory_stats = log_memory_usage()
    
    # Validate return value and no exceptions
    assert isinstance(memory_stats, dict)
    assert 'total' in memory_stats
    assert 'percent' in memory_stats

def test_memory_stats_accuracy():
    # Compare with psutil's direct memory stats
    memory_stats = log_memory_usage()
    system_memory = psutil.virtual_memory()
    
    # Allow small floating-point discrepancies
    assert abs(memory_stats['total'] - system_memory.total / (1024 * 1024)) < 1
    assert abs(memory_stats['percent'] - system_memory.percent) < 1