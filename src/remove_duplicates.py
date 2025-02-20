def remove_duplicates_and_sort(arr):
    """
    Remove duplicate elements from an array and sort in ascending order
    without using built-in sorting or duplicate removal methods.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Sorted list with duplicates removed
    """
    # Handle empty list case
    if not arr:
        return []
    
    # First, remove duplicates using a manual approach
    unique_elements = []
    for num in arr:
        # Only add if the number is not already in the unique_elements list
        if num not in unique_elements:
            unique_elements.append(num)
    
    # Manual bubble sort to sort the unique elements in ascending order
    n = len(unique_elements)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if unique_elements[j] > unique_elements[j + 1]:
                unique_elements[j], unique_elements[j + 1] = unique_elements[j + 1], unique_elements[j]
    
    return unique_elements