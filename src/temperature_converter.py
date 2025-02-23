def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit degrees.

    Returns:
        float: Temperature converted to Celsius.

    Raises:
        TypeError: If input is not a number.
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a numeric value")
    
    return (fahrenheit - 32) * 5/9