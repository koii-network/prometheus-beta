def tim_sort(arr):
    """
    Implement Tim Sort algorithm for sorting a list.
    
    Tim Sort is a hybrid sorting algorithm that combines merge sort and insertion sort.
    It's the standard sorting algorithm used in Python's sorted() and list.sort() methods.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    """
    # If list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Define the minimum run length (typically between 32 and 64)
    MIN_MERGE = 32
    
    def insertion_sort(arr, left, right):
        """
        Perform insertion sort on a small section of the array.
        
        Args:
            arr (list): The list to be partially sorted
            left (int): Starting index of the section
            right (int): Ending index of the section
        """
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def merge(arr, left, mid, right):
        """
        Merge two sorted subarrays.
        
        Args:
            arr (list): The list containing subarrays to merge
            left (int): Starting index of the first subarray
            mid (int): Ending index of the first subarray
            right (int): Ending index of the second subarray
        """
        # Create temporary arrays
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        
        # Initial indexes of first and second subarrays
        i, j, k = 0, 0, left
        
        # Merge the temporary arrays back into arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        
        # Copy remaining elements of right_arr if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
    
    def tim_sort_recursive(arr, left, right):
        """
        Recursive implementation of Tim Sort.
        
        Args:
            arr (list): The list to be sorted
            left (int): Starting index
            right (int): Ending index
        """
        # If the section is small, use insertion sort
        if right - left + 1 < MIN_MERGE:
            insertion_sort(arr, left, right)
            return
        
        # Find the midpoint
        mid = left + (right - left) // 2
        
        # Recursively sort first and second halves
        tim_sort_recursive(arr, left, mid)
        tim_sort_recursive(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Call the recursive Tim Sort implementation
    tim_sort_recursive(sorted_arr, 0, len(sorted_arr) - 1)
    
    return sorted_arr