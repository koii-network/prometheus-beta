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
    # Leonardo numbers (used in heap construction)
    leonardo_numbers = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219]
    
    def sift_down(low, high, root):
        """
        Perform sift down operation in Leonardo heap
        """
        r = root
        while True:
            if r >= high:
                return
            
            if r + 1 < high and arr[r] < arr[r + 1]:
                large_child = r + 1
            else:
                large_child = r
            
            if arr[r] < arr[large_child]:
                arr[r], arr[large_child] = arr[large_child], arr[r]
                r = large_child
            else:
                break
    
    def heapify(start, length):
        """
        Convert the array into a smooth sort heap
        """
        m = length - 1
        for i in range(m, start - 1, -1):
            sift_down(start, length, i)
    
    # If array is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Initialize smooth sort
    sorted_len = 0
    size = [0]
    roots = [0]
    
    # Build heap
    for i in range(len(arr)):
        if sorted_len > 0 and (len(size) == 1 or 
                                (len(size) > 1 and size[-1] > size[-2] + 1)):
            heapify(roots[-1], i + 1)
            size.append(size[-1] + 1)
            roots.append(roots[-1])
        else:
            heapify(i, i + 1)
            size.append(1)
            roots.append(i)
        
        sorted_len = i + 1
    
    # Extract elements in sorted order
    for i in range(len(arr) - 1, 0, -1):
        if sorted_len > 0:
            arr[i], arr[roots[-1]] = arr[roots[-1]], arr[i]
            sorted_len -= 1
            size[-1] -= 1
            
            if size[-1] == 0:
                size.pop()
                roots.pop()
            else:
                sift_down(roots[-1], i, roots[-1])
    
    return arr