import functools
import logging
import time

def log_function_call(logger=None):
    """
    A decorator to log function entry and exit with optional custom logger.
    
    :param logger: Optional custom logger. If not provided, uses default logging.
    :return: Decorator function
    """
    if logger is None:
        # Configure default logging if no logger is provided
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log function entry with arguments
            func_args_repr = [repr(a) for a in args]
            func_kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(func_args_repr + func_kwargs_repr)
            
            logger.info(f"Entering function: {func.__name__}({signature})")
            start_time = time.time()

            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Log function exit and execution time
                end_time = time.time()
                execution_time = end_time - start_time
                logger.info(f"Exiting function: {func.__name__}. Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                raise

        return wrapper
    return decorator