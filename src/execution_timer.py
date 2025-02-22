import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_execution_time(func):
    """
    A decorator that logs the execution time of a function.
    
    Args:
        func (callable): The function to be timed and logged.
    
    Returns:
        callable: A wrapped function that logs its execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logging.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
            return result
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            logging.error(f"Function '{func.__name__}' raised an exception after {execution_time:.4f} seconds: {str(e)}")
            raise
    return wrapper