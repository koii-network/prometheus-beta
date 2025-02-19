def analyze_numbers(numbers):
    """
    Analyze a list of numbers to calculate the sum of even numbers and count of odd numbers.
    
    Args:
        numbers (list): A list of integers to analyze
    
    Returns:
        tuple: A tuple containing two elements:
            - Sum of all even numbers in the list
            - Count of odd numbers in the list
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    
    return even_sum, odd_count