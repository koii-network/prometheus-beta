def product_left_array(nums):
    """
    Returns an array where each element is the product of numbers to the left 
    of the corresponding element in the original array.
    
    Args:
        nums (list): Input list of numbers
    
    Returns:
        list: Array with products of numbers to the left of each element
    """
    # Handle edge cases
    if not nums:
        return []
    
    # Initialize result array with 1s
    result = [1] * len(nums)
    
    # Calculate prefix products from left to right
    left_product = 1
    for i in range(len(nums)):
        # Multiply the current element by the product of all elements to its left
        result[i] = left_product
        # Update left_product for next iteration
        left_product *= nums[i]
    
    return result