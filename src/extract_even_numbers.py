def extract_even_numbers(numbers):
    """
    Extract even numbers from a list of integers in linear time complexity.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A new list containing only the even numbers from the input list
    """
    # Create an empty list to store even numbers
    even_numbers = []
    
    # Iterate through the input list once (linear time complexity O(n))
    for num in numbers:
        # Check if the number is even by using modulo operator
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers