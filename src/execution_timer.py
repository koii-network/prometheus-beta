import time
import functools
import logging

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
        # Configure logging if not already configured
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Record start time
        start_time = time.time()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and log execution time
            end_time = time.time()
            execution_time = end_time - start_time
            logging.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur
            logging.error(f"Error in function '{func.__name__}': {str(e)}")
            raise
    
    return wrapper