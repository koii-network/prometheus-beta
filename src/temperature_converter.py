def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.

    Raises:
        TypeError: If input is not a number.
    """
    # Check if input is a number
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number")
    
    # Conversion formula: (°F - 32) × 5/9 = °C
    celsius = (fahrenheit - 32) * 5 / 9
    
    return round(celsius, 2)