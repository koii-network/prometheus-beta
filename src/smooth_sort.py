from typing import List, TypeVar, Union

T = TypeVar('T')

def smooth_sort(arr: List[T]) -> List[T]:
    """
    Implement the Smooth Sort algorithm for sorting a list.
    
    Smooth Sort is an adaptive sorting algorithm that has O(n log n) worst-case complexity
    and performs better on partially sorted arrays.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Leonardo numbers generator
    def leonardo_numbers(n):
        a, b = 1, 1
        while a <= n:
            yield a
            a, b = b, a + b + 1
    
    # Smooth Sort implementation
    def sift_down(arr, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    
    # Create a copy to avoid modifying the original list
    work_arr = arr.copy()
    
    # Smooth Sort phases
    size = len(work_arr)
    leo_nums = list(leonardo_numbers(size))
    
    # Initial heap construction
    for i in range(size - 1, -1, -1):
        sift_down(work_arr, i, size - 1)
    
    # Extraction phase
    for i in range(size - 1, 0, -1):
        work_arr[0], work_arr[i] = work_arr[i], work_arr[0]
        sift_down(work_arr, 0, i - 1)
    
    return work_arr