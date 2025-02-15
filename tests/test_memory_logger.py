import logging
import pytest
from unittest.mock import Mock, patch
import memory_profiler

from src.memory_logger import log_memory_usage

def test_log_memory_usage_default_logger():
    """Test memory logging with default logger"""
    @log_memory_usage()
    def sample_function():
        # Allocate some memory
        return [i for i in range(10000)]
    
    with patch('memory_profiler.memory_usage', side_effect=[[100], [200]]):
        with patch('logging.Logger.info') as mock_log:
            result = sample_function()
            
            assert result == list(range(10000))
            
            # Verify logging calls
            assert mock_log.call_count == 3
            calls = mock_log.call_args_list
            assert "Memory before sample_function" in calls[0][0][0]
            assert "Memory after sample_function" in calls[1][0][0]
            assert "Memory change in sample_function" in calls[2][0][0]

def test_log_memory_usage_custom_logger():
    """Test memory logging with custom logger"""
    custom_logger = Mock(spec=logging.Logger)
    
    @log_memory_usage(logger=custom_logger)
    def another_function():
        return 42
    
    with patch('memory_profiler.memory_usage', side_effect=[[50], [75]]):
        result = another_function()
        
        assert result == 42
        
        # Verify custom logger calls
        assert custom_logger.info.call_count == 3
        calls = custom_logger.info.call_args_list
        assert "Memory before another_function" in calls[0][0][0]
        assert "Memory after another_function" in calls[1][0][0]
        assert "Memory change in another_function" in calls[2][0][0]

def test_log_memory_usage_with_args():
    """Test memory logging with function having arguments"""
    @log_memory_usage()
    def func_with_args(x, y):
        return x + y
    
    with patch('memory_profiler.memory_usage', side_effect=[[10], [20]]):
        with patch('logging.Logger.info') as mock_log:
            result = func_with_args(3, 4)
            
            assert result == 7
            assert mock_log.call_count == 3