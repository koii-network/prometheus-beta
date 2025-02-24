import logging
import functools
import time

def log_function_call(logger=None):
    """
    A decorator to log function entry, exit, and execution time.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorated function
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Prepare input arguments representation
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            
            # Log function entry
            logger.info(f"Entering: {func.__name__}({signature})")
            
            # Track start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log function exit and result
                logger.info(f"Exiting: {func.__name__}. Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator