def smooth_sort(arr):
    """
    Implement the Smooth Sort algorithm for sorting a list.
    
    Smooth Sort is an adaptive sorting algorithm that performs well on 
    partially sorted arrays by using Leonardo heaps.
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list
    """
    def leonardo_search(n):
        """Find the Leonardo number less than or equal to n"""
        i = 0
        while True:
            if i >= len(leonardo_numbers):
                break
            if leonardo_numbers[i] > n:
                break
            i += 1
        return i - 1

    # Leonardo numbers (used in heap construction)
    leonardo_numbers = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219]
    
    # Optimization for small lists
    if len(arr) <= 1:
        return arr

    # Initial state of Leonardo tree
    b_tree = 0  # bitmap of Leonardo trees
    size = 1    # size of current tree
    p = 1       # previous Leonardo tree size

    # Build the Leonardo heap
    for i in range(1, len(arr)):
        if b_tree & 3 == 3:
            b_tree >>= 2
            size += p
            p = leonardo_numbers[leonardo_search(p)]
        else:
            if leonardo_search(size + 1) == leonardo_search(p + 1) + 1:
                b_tree <<= 1
                size += 1
                p = leonardo_numbers[leonardo_search(p + 1)]
            else:
                b_tree = (b_tree << 1) | 1
                size += 1

        # Sift the current element into its correct position
        j = i
        while j > 0 and arr[j - size] > arr[j]:
            arr[j - size], arr[j] = arr[j], arr[j - size]
            j -= size
            k = leonardo_search(size)
            size = leonardo_numbers[k - 1] if k > 0 else 1
            p = leonardo_numbers[k - 2] if k > 1 else 1

    # Deheap and final sort
    for i in range(len(arr) - 1, 0, -1):
        if b_tree & 1 == 1:
            b_tree >>= 1
        else:
            k = leonardo_search(size + 1)
            next_size = leonardo_numbers[k - 1] if k > 0 else 1
            next_p = leonardo_numbers[k - 2] if k > 1 else 1

            if next_size > i:
                break

            b_tree = (b_tree >> 1) | (1 << (k + 1))
            size = next_size
            p = next_p

            # Sift down operation
            j = i - size
            while j > 0 and arr[j] > arr[j + size]:
                arr[j], arr[j + size] = arr[j + size], arr[j]
                j -= size
                k = leonardo_search(size)
                size = leonardo_numbers[k - 1] if k > 0 else 1
                p = leonardo_numbers[k - 2] if k > 1 else 1

    return arr