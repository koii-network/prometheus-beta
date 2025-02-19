def analyze_numbers(numbers):
    """
    Analyze a list of numbers by summing even numbers and counting odd numbers.
    
    Args:
        numbers (list): A list of integers to analyze.
    
    Returns:
        tuple: A tuple containing two elements:
            - Sum of all even numbers in the list
            - Count of odd numbers in the list
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Validate list contains only numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers")
    
    # Calculate sum of even numbers and count of odd numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    
    return even_sum, odd_count