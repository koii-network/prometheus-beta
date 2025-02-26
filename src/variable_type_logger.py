import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.
    
    Args:
        variable: Any Python variable to log the type of.
    
    Returns:
        str: The string representation of the variable's type.
    """
    # Get the type of the variable
    variable_type = type(variable).__name__
    
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - Variable Type Logger - %(levelname)s: %(message)s')
    
    # Log the type of the variable
    logging.info(f"Variable type: {variable_type}")
    
    return variable_type