def product_except_self(nums):
    """
    Calculate an array where each element is the product of all other elements 
    except the current element.
    
    Args:
        nums (list): Input list of numbers
    
    Returns:
        list: Array with products of all other elements except current
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numeric")
    
    # Handle empty or single-element list
    if len(nums) <= 1:
        return [1] * len(nums)
    
    # Initialize result array and temporary variables
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    
    # Calculate right products
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result