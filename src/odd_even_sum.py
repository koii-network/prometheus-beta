def calculate_odd_even_sum(numbers):
    """
    Calculate the sum of odd and even numbers in the given array.
    
    Args:
        numbers (list): An array of integers
    
    Returns:
        tuple: A tuple containing (sum of odd numbers, sum of even numbers)
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Initialize sum variables
    odd_sum = 0
    even_sum = 0
    
    # Iterate through the numbers and sum odd and even numbers
    for num in numbers:
        # Validate each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        # Check if number is odd or even and add to respective sum
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return odd_sum, even_sum