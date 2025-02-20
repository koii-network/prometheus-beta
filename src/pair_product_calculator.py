from typing import List, Tuple

def calculate_pair_products(numbers: List[int]) -> List[Tuple[Tuple[int, int], int]]:
    """
    Calculate the product of all possible pairs of elements in the given list.
    
    Args:
        numbers (List[int]): A list of integers
    
    Returns:
        List[Tuple[Tuple[int, int], int]]: A list of tuples, where each tuple contains:
            - A tuple of the two numbers forming the pair
            - The product of those two numbers
    
    Examples:
        >>> calculate_pair_products([1, 2, 3])
        [((1, 2), 2), ((1, 3), 3), ((2, 3), 6)]
        >>> calculate_pair_products([])
        []
        >>> calculate_pair_products([5])
        []
    """
    # If the list has fewer than 2 elements, return an empty list
    if len(numbers) < 2:
        return []
    
    # Use list comprehension to generate all unique pairs and their products
    pair_products = [
        ((numbers[i], numbers[j]), numbers[i] * numbers[j])
        for i in range(len(numbers))
        for j in range(i+1, len(numbers))
    ]
    
    return pair_products