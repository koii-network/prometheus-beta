def remove_duplicates_and_sort(arr):
    """
    Remove duplicate elements from an array and sort in ascending order
    without using built-in sorting or removal methods.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed and sorted in ascending order
    """
    # Handle empty or None input
    if not arr:
        return []
    
    # Remove duplicates using a manual approach
    unique_elements = []
    for num in arr:
        # Check if the number is already in unique_elements
        if num not in unique_elements:
            unique_elements.append(num)
    
    # Manual bubble sort to sort the unique elements
    n = len(unique_elements)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_elements[j] > unique_elements[j + 1]:
                # Swap elements
                unique_elements[j], unique_elements[j + 1] = unique_elements[j + 1], unique_elements[j]
    
    return unique_elements