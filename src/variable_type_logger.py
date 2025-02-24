import logging

def log_variable_type(variable):
    """
    Log the type of the given variable.

    Args:
        variable (Any): The variable whose type needs to be logged.

    Returns:
        type: The type of the input variable.

    Raises:
        TypeError: If the input is None.
    """
    # Check for None first
    if variable is None:
        logging.error("Input variable is None")
        raise TypeError("Input variable cannot be None")

    # Get the type of the variable
    var_type = type(variable)

    # Log the type
    logging.info(f"Variable type: {var_type.__name__}")

    return var_type