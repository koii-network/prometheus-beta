def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order. Defaults to True.
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains incomparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    def bitonic_merge(sub_arr, ascending):
        """Merge a bitonic sequence"""
        if len(sub_arr) <= 1:
            return sub_arr
        
        mid = len(sub_arr) // 2
        
        # Compare and swap elements
        for i in range(mid):
            if (ascending and sub_arr[i] > sub_arr[i + mid]) or \
               (not ascending and sub_arr[i] < sub_arr[i + mid]):
                sub_arr[i], sub_arr[i + mid] = sub_arr[i + mid], sub_arr[i]
        
        # Recursively sort first and second halves
        first_half = bitonic_merge(sub_arr[:mid], ascending)
        second_half = bitonic_merge(sub_arr[mid:], ascending)
        
        return first_half + second_half
    
    def bitonic_sort_recursive(arr, ascending):
        """Recursive implementation of bitonic sort"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        
        # Recursively sort first half in ascending order
        first_half = bitonic_sort_recursive(arr[:mid], True)
        # Recursively sort second half in descending order
        second_half = bitonic_sort_recursive(arr[mid:], False)
        
        # Combine the two halves
        full_sequence = first_half + second_half
        
        # Merge the bitonic sequence
        return bitonic_merge(full_sequence, ascending)
    
    # Create a copy to avoid modifying the original list
    result = bitonic_sort_recursive(arr.copy(), ascending)
    
    return result