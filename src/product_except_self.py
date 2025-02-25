def product_except_self(nums):
    """
    Calculate a list where each element is the product of all other elements except itself.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        list: A list where each element is the product of all other elements except the element at that index
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input contains non-numeric types
    
    Examples:
        >>> product_except_self([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> product_except_self([2, 3, 4, 5])
        [60, 40, 30, 24]
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric types
    if any(not isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numeric")
    
    # Special case for empty or single-element list
    if len(nums) <= 1:
        return [1] if nums else []
    
    # Solution using O(n) time and O(1) extra space (excluding output)
    n = len(nums)
    
    # Initialize output list
    output = [1] * n
    
    # Calculate prefix products from left to right
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    
    # Calculate postfix products from right to left and combine with prefix products
    postfix = 1
    for i in range(n-1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    
    return output