def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius degrees
    
    Returns:
        float: Temperature converted to Fahrenheit
    
    Raises:
        TypeError: If input is not a number
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    
    return (celsius * 9/5) + 32