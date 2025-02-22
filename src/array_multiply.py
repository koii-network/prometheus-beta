def multiply(arr):
    """
    Multiply corresponding elements of input arrays.
    
    Args:
        arr (list): A list of lists of numbers to multiply
    
    Returns:
        list: A new list with elements multiplied
    
    Raises:
        ValueError: If input is not a list of lists or lists have different lengths
    """
    # Check if input is a valid list of lists
    if not isinstance(arr, list) or not arr:
        return []
    
    # Check if all elements are lists
    if not all(isinstance(sublist, list) for sublist in arr):
        raise ValueError("Input must be a list of lists")
    
    # Check if all sublists have the same length
    if len(set(len(sublist) for sublist in arr)) > 1:
        raise ValueError("All input lists must have the same length")
    
    # If input checks pass, perform element-wise multiplication
    return [
        # Multiply corresponding elements for each position
        1 if not arr else 
        # Use 1 as initial value to handle empty input
        prod([arr[i][j] for i in range(len(arr))])
        # Calculate product of each column across sublists 
        for j in range(len(arr[0]))
    ]

def prod(numbers):
    """
    Calculate the product of a list of numbers.
    
    Args:
        numbers (list): List of numbers to multiply
    
    Returns:
        number: Product of all numbers in the list
    """
    result = 1
    for num in numbers:
        result *= num
    return result