def tim_sort(arr):
    """
    Implement Tim Sort algorithm for sorting a list.
    
    Tim Sort is a hybrid sorting algorithm that combines Insertion Sort 
    and Merge Sort to provide efficient sorting.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list 
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Minimum run length for Tim Sort
    MIN_RUN = 32
    
    def insertion_sort(arr, left=0, right=None):
        """
        Perform insertion sort on a sub-array
        
        Args:
            arr (list): The list to be sorted
            left (int): Starting index of the sub-array
            right (int): Ending index of the sub-array
        
        Returns:
            list: Partially sorted list
        """
        if right is None:
            right = len(arr) - 1
        
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr
    
    def merge(arr, left, mid, right):
        """
        Merge two sorted sub-arrays
        
        Args:
            arr (list): The list containing sub-arrays to merge
            left (int): Starting index of left sub-array
            mid (int): Ending index of left sub-array
            right (int): Ending index of right sub-array
        
        Returns:
            list: Merged and sorted list
        """
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        
        # Copy remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
        
        return arr
    
    # Determine run size and perform insertion sort on runs
    n = len(arr)
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Merge runs of size MIN_RUN
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge the two runs
            if mid < end:
                merge(arr, start, mid, end)
        
        size *= 2
    
    return arr