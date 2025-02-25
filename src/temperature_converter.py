def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius, rounded to 2 decimal places
    
    Raises:
        TypeError: If input is not a number
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number")
    
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)