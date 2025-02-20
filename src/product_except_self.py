def product_except_self(nums):
    """
    Returns a list where each element is the product of all other elements except itself.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list where each element is the product of all other elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All list elements must be numeric")
    
    # Handle empty list and single-element list cases
    if len(nums) <= 1:
        return [1] * len(nums)
    
    # Calculate prefix and suffix products
    n = len(nums)
    prefix_products = [1] * n
    suffix_products = [1] * n
    result = [1] * n
    
    # Calculate prefix products
    for i in range(1, n):
        prefix_products[i] = prefix_products[i-1] * nums[i-1]
    
    # Calculate suffix products
    for i in range(n-2, -1, -1):
        suffix_products[i] = suffix_products[i+1] * nums[i+1]
    
    # Combine prefix and suffix products
    for i in range(n):
        result[i] = prefix_products[i] * suffix_products[i]
    
    return result