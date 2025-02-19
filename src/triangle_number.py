def triangle_number(num):
    """
    Determine if a number is a Triangle Number.
    
    A Triangle Number is a number that can be represented as the sum of its proper divisors.
    Proper divisors are positive divisors of the number excluding the number itself.
    
    Args:
        num (int): The number to check for being a Triangle Number.
    
    Returns:
        bool: True if the number is a Triangle Number, False otherwise.
    """
    # Handle edge cases
    if num <= 0:
        return False
    
    # Find proper divisors and calculate their sum
    proper_divisors = [i for i in range(1, num) if num % i == 0]
    divisor_sum = sum(proper_divisors)
    
    # Check if the sum of proper divisors equals the original number
    return divisor_sum == num