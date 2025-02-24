def sort_nums(nums):
    """
    Inefficient sorting function with a known bug.
    Intentionally includes a bug to demonstrate performance issues.
    
    Args:
        nums (list): A list of numbers to be sorted.
    
    Returns:
        list: Partially or incorrectly sorted list.
    """
    n = len(nums)
    for i in range(n):
        # Intentional bug: Only compare with next element, leading to incorrect sorting
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                # Swap elements
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def optimal_sort(nums):
    """
    Improved sorting implementation using Python's built-in Timsort algorithm.
    
    Args:
        nums (list): A list of numbers to be sorted.
    
    Returns:
        list: Correctly sorted list in ascending order.
    """
    return sorted(nums)