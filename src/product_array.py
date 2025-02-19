def calculate_left_product_array(nums):
    """
    Calculate an array where each element is the product of numbers to the left of the original element.
    
    Args:
        nums (list): Input list of numbers
    
    Returns:
        list: A new list where each element is the product of numbers to its left
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numeric")
    
    # Handle empty list case
    if not nums:
        return []
    
    # Initialize result array
    result = [1] * len(nums)
    
    # Calculate cumulative product from left
    left_product = 1
    for i in range(len(nums)):
        # Use the current left_product for the current index
        result[i] = left_product
        # Update left_product for next iteration
        left_product *= nums[i]
    
    return result