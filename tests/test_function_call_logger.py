import pytest
from src.function_call_logger import FunctionCallLogger

def test_function_call_logger():
    # Create a logger instance
    logger = FunctionCallLogger()
    
    # Test function to decorate
    @logger.log_calls
    def sample_function(x, y):
        return x + y
    
    # Initial call count should be 0
    assert logger.get_call_count('sample_function') == 0
    
    # Call the function multiple times
    sample_function(1, 2)
    sample_function(3, 4)
    sample_function(5, 6)
    
    # Verify call count
    assert logger.get_call_count('sample_function') == 3

def test_multiple_decorated_functions():
    # Create a logger instance
    logger = FunctionCallLogger()
    
    # Decorate multiple functions
    @logger.log_calls
    def func1():
        pass
    
    @logger.log_calls
    def func2():
        pass
    
    # Call functions
    func1()
    func1()
    func2()
    
    # Verify individual call counts
    assert logger.get_call_count('func1') == 2
    assert logger.get_call_count('func2') == 1

def test_reset_call_count():
    # Create a logger instance
    logger = FunctionCallLogger()
    
    @logger.log_calls
    def test_func():
        pass
    
    # Call function multiple times
    test_func()
    test_func()
    test_func()
    
    # Verify initial count
    assert logger.get_call_count('test_func') == 3
    
    # Reset specific function count
    logger.reset_call_count('test_func')
    assert logger.get_call_count('test_func') == 0
    
    # Reset all function counts
    test_func()
    logger.reset_call_count()
    assert logger.get_call_count('test_func') == 0

def test_thread_safety():
    import threading
    
    # Create a logger instance
    logger = FunctionCallLogger()
    
    @logger.log_calls
    def increment_func():
        pass
    
    # Function to call the decorated function multiple times
    def worker():
        for _ in range(1000):
            increment_func()
    
    # Create multiple threads
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    # Verify total call count
    assert logger.get_call_count('increment_func') == 10000