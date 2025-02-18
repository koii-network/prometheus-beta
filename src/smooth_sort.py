def smooth_sort(arr):
    """
    Implement the Smooth Sort algorithm for sorting a list.
    
    Smooth Sort is a comparison-based sorting algorithm that is an adaptive, 
    in-place sorting algorithm with O(n log n) worst-case time complexity.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    """
    # If the input is None or empty, return an empty list
    if arr is None:
        return []
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Leonardo numbers sequence (used in Smooth Sort)
    leonardo_numbers = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219]
    
    def sift_down(start, length, r):
        """
        Perform the sift down operation for heap refinement
        """
        root = start
        while r >= 2:
            child = root * 2 + 1
            if child < length:
                if child + 1 < length and arr[child] < arr[child + 1]:
                    child += 1
                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child
                    r -= 1
                else:
                    break
            else:
                break
    
    def smooth_sort_internal():
        """
        Internal sorting logic
        """
        # Number of elements
        n = len(arr)
        
        # Initial configuration
        q = 1  # Number of trees
        r = 0  # Largest Leonardo number index
        p = 1  # Total number of nodes
        
        # Find the initial Leonardo tree configuration
        while p < n:
            if (q & 1) == 0:
                p += leonardo_numbers[r]
                r += 1
                q //= 2
            else:
                if (q & 2) == 0:
                    p += leonardo_numbers[r - 1]
                else:
                    p += leonardo_numbers[r]
                
                # Adjust configuration and sift
                if r > 0:
                    r -= 1
                    q //= 2
                    
                    # Sift down the current subtree
                    sift_down(p - leonardo_numbers[r], n, r)
                else:
                    break
        
        # Heapify and extract elements
        while p > 1:
            p -= 1
            
            if r <= 0:
                break
            
            if (q & 1) == 0:
                p -= leonardo_numbers[r]
                r += 1
                q //= 2
            else:
                p -= leonardo_numbers[r - 1]
                
                if r > 0:
                    sift_down(p, n, r - 1)
                    r -= 1
                    q //= 2
        
    # Call the internal sorting method
    smooth_sort_internal()
    
    return arr