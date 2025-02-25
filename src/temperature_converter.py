def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius degrees
    
    Returns:
        float: Temperature converted to Fahrenheit
    
    Raises:
        TypeError: If input is not a number
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit