def smooth_sort(arr):
    """
    Implement the Smooth Sort algorithm for sorting a list.
    
    Smooth Sort is a comparison-based sorting algorithm that is an adaptive, 
    comparison-sorting algorithm with an O(n log n) worst-case time complexity.
    It's similar to Heap Sort but with better performance on partially sorted arrays.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    """
    # If the input is None or empty, return an empty list
    if arr is None:
        return []
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Leonardo numbers are key to the smooth sort algorithm
    leonardo_numbers = [1, 1]
    while leonardo_numbers[-1] < len(arr):
        leonardo_numbers.append(leonardo_numbers[-1] + leonardo_numbers[-2] + 1)
    
    # Recursive heapify function to maintain the Leonardo heap property
    def heapify(start, length, state):
        r = start
        while r > 0:
            # Determine which Leonardo tree to process
            if (state & 3) == 0:
                r -= 1
                state >>= 2
            elif (state & 3) == 1:
                if r == 1:
                    break
                r -= 2
                state = (state >> 2) | (2 << (2 * r))
            else:
                r -= 1
                if r == 1:
                    break
                state = (state >> 2) | (1 << (2 * r))
            
            # Compare and swap if needed
            child = start - leonardo_numbers[r]
            if arr[child] > arr[start]:
                arr[child], arr[start] = arr[start], arr[child]
                start = child
            else:
                break
        return state
    
    # Sorting phase
    state = 0
    for i in range(len(arr)):
        # Merge adjacent Leonardo trees
        if (state & 3) == 3:
            state >>= 2
            state |= 1 << (2 * (len(leonardo_numbers) - 1))
            heapify(i, len(arr), state)
        
        # Add new tree
        state = ((state << 2) | 1) & ((1 << (2 * len(leonardo_numbers))) - 1)
    
    # Deheap phase (convert Leonardo heap to sorted array)
    for i in range(len(arr) - 1, 0, -1):
        state = heapify(i, len(arr), state)
        if (state & 3) == 1:
            state >>= 2
    
    return arr