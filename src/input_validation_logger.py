import logging
import functools
import inspect

def log_input_validation(logger=None):
    """
    A decorator to log input validation messages and errors.
    
    :param logger: Optional logger. If not provided, creates a default logger.
    :return: Decorator function for input validation logging
    """
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # Create console handler if no handler exists
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function's signature
            sig = inspect.signature(func)
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Log input validation start
            logger.info(f"Validating inputs for function: {func.__name__}")
            
            # Log each parameter and its value
            for param_name, param_value in bound_arguments.arguments.items():
                logger.info(f"Parameter '{param_name}': {param_value}")
            
            try:
                # Call the original function
                result = func(*args, **kwargs)
                
                # Log successful validation
                logger.info(f"Input validation successful for function: {func.__name__}")
                
                return result
            
            except TypeError as e:
                # Log type-related validation errors
                logger.error(f"Type validation error in {func.__name__}: {str(e)}")
                raise
            
            except ValueError as e:
                # Log value-related validation errors
                logger.error(f"Value validation error in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator