def sort_nums(numbers):
    """
    A sorting function with an intentional bug for demonstration purposes.
    Bug: Incorrect sorting for lists with duplicate elements.
    
    Args:
        numbers (list): A list of numbers to be sorted.
    
    Returns:
        list: Partially or incorrectly sorted list.
    """
    n = len(numbers)
    # Intentionally buggy bubble sort with a flaw in handling duplicates
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def optimal_sort(numbers):
    """
    An optimal sorting implementation using Python's built-in sorting algorithm.
    
    Args:
        numbers (list): A list of numbers to be sorted.
    
    Returns:
        list: Correctly sorted list in ascending order.
    """
    return sorted(numbers)