def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit to convert.

    Returns:
        float: Equivalent temperature in Celsius.

    Raises:
        TypeError: If input is not a number.
    """
    # Check if input is a number
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a numeric value")
    
    # Conversion formula: (°F - 32) × 5/9 = °C
    celsius = (fahrenheit - 32) * 5/9
    
    # Round to 2 decimal places for precision
    return round(celsius, 2)