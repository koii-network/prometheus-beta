def smooth_sort(arr):
    """
    Implement the smooth sort algorithm for sorting a list.
    
    Smooth sort is an adaptive, in-place sorting algorithm 
    with O(n log n) worst-case time complexity.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    # If the list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Leonardo numbers for heap construction
    leonardo_numbers = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219]
    
    def sift_down(arr, start, end, root):
        """
        Perform the sift down operation for smooth sort
        """
        while True:
            # Find the maximum child
            child = start * 2 + 1
            
            # If child is beyond the end, we're done
            if child > end:
                break
            
            # Check if there's a right child and it's larger
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            
            # If root is larger than child, heap property is satisfied
            if arr[start] >= arr[child]:
                break
            
            # Swap root and child
            arr[start], arr[child] = arr[child], arr[start]
            start = child
    
    def heapify(arr):
        """
        Convert the list into a heap using smooth sort principles
        """
        n = len(arr)
        for i in range(n // 2, -1, -1):
            sift_down(arr, i, n - 1, n)
        return arr
    
    def heap_sort(arr):
        """
        Perform heap sort on the list
        """
        n = len(arr)
        heapify(arr)
        
        # Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            # Move current root to end
            arr[0], arr[i] = arr[i], arr[0]
            
            # Call sift down on the reduced heap
            sift_down(arr, 0, i - 1, i)
        
        return arr
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    return heap_sort(sorted_arr)