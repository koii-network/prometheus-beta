import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.

    This function takes any variable as input and logs its type using the 
    standard Python logging module. It provides a simple way to inspect 
    the type of a variable during runtime.

    Args:
        variable (Any): The variable whose type needs to be logged.

    Returns:
        type: The type of the input variable.

    Example:
        >>> x = 42
        >>> log_variable_type(x)
        # This would log: INFO:root:Variable type is: <class 'int'>
    """
    # Configure basic logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(levelname)s:%(name)s:Variable type is: %(message)s')
    
    # Get the type of the variable
    var_type = type(variable)
    
    # Log the type
    logging.info(str(var_type))
    
    return var_type