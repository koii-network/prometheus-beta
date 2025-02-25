import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.
    
    Args:
        variable: Any Python object to log the type of
    
    Returns:
        str: The string representation of the variable's type
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Get the type of the variable
    var_type = type(variable).__name__
    
    # Log the type
    logging.info(f"Variable type: {var_type}")
    
    return var_type