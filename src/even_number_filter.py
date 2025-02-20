def filter_even_numbers(numbers):
    """
    Filter even numbers from an input list using linear time complexity.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A new list containing only even numbers from the input list
    """
    # Create a new list to store even numbers
    even_numbers = []
    
    # Iterate through the input list once (linear time complexity O(n))
    for num in numbers:
        # Check if the number is even by using the modulo operator
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers