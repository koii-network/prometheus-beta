def product_except_self(nums):
    """
    Returns a list where each element is the product of all other elements except itself.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        list: A list where each element is the product of all other elements except the element at that index
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("List must contain only numeric elements")
    
    # Handle empty list
    if not nums:
        return []
    
    # Handle list with single element
    if len(nums) == 1:
        return [1]
    
    # Calculate left products
    left_products = [1] * len(nums)
    for i in range(1, len(nums)):
        left_products[i] = left_products[i-1] * nums[i-1]
    
    # Calculate right products and final result
    right_product = 1
    result = [1] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] = left_products[i] * right_product
        right_product *= nums[i]
    
    return result