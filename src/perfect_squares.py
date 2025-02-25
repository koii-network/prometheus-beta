import math

def sum_perfect_squares_from_set(num_set):
    """
    Calculate the sum of all perfect squares that can be formed from integers in the given set.
    
    Args:
        num_set (set or iterable): A set of integers to check for perfect squares.
    
    Returns:
        int: The sum of all unique perfect squares that can be formed from the set.
    
    Raises:
        TypeError: If the input is not a set or contains non-integer elements.
    """
    # Input validation
    if not isinstance(num_set, (set, list, tuple)):
        raise TypeError("Input must be a set, list, or tuple of integers")
    
    # Convert to set to remove duplicates and ensure integer type
    try:
        num_set = set(map(int, num_set))
    except (TypeError, ValueError):
        raise TypeError("All elements must be convertible to integers")
    
    # Find all perfect squares
    perfect_squares = set()
    for num in num_set:
        if num < 0:
            continue  # Skip negative numbers
        
        # Check if the number is a perfect square
        root = int(math.sqrt(num))
        if root * root == num:
            perfect_squares.add(num)
        
        # Check perfect squares that can be formed by combining set elements
        for other in num_set:
            if other < 0:
                continue
            
            combined = num * other
            combined_root = int(math.sqrt(combined))
            if combined_root * combined_root == combined:
                perfect_squares.add(combined)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)