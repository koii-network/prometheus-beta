def sort_nums(numbers):
    """
    Sorting function with a known bug (inefficient and potentially incorrect implementation)
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: Partially or incorrectly sorted list
    """
    # Intentional bug: Simple but incorrect sorting method
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers[:len(numbers)//2]  # Another intentional bug - returns only half the list

def optimal_sort(numbers):
    """
    Optimal sorting implementation with improved time complexity
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: Fully and correctly sorted list
    """
    # Use Python's built-in Timsort algorithm, which has O(n log n) time complexity
    return sorted(numbers)