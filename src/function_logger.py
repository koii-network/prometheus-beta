import functools
import logging
import time

def log_execution(logger=None):
    """
    A decorator to log function execution start and end times.
    
    :param logger: Optional logger. If not provided, uses default logging.
    :return: Decorated function that logs execution details
    """
    if logger is None:
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log function start
            logger.info(f"Executing function: {func.__name__}")
            logger.info(f"Arguments: args={args}, kwargs={kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Log function end and execution time
                end_time = time.time()
                execution_time = end_time - start_time
                logger.info(f"Function {func.__name__} completed successfully")
                logger.info(f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator