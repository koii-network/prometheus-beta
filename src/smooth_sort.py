from typing import List, TypeVar, Comparable

T = TypeVar('T', bound=Comparable)

def smooth_sort(arr: List[T]) -> List[T]:
    """
    Implements the Smooth Sort algorithm for sorting a list.
    
    Args:
        arr (List[T]): The input list to be sorted.
    
    Returns:
        List[T]: The sorted list.
    """
    # If the list is empty or has only one element, return it as-is
    if len(arr) <= 1:
        return arr

    # Leonardo numbers (used for heap sizes)
    leonardo_numbers = [1, 1]
    while leonardo_numbers[-1] < len(arr):
        leonardo_numbers.append(leonardo_numbers[-1] + leonardo_numbers[-2] + 1)

    # Initialize state
    heap_count = 0
    heap_sizes = [0] * len(leonardo_numbers)

    # Convert array to heap
    for i in range(len(arr)):
        if heap_count > 0 and (heap_count < 2 or 
            (heap_sizes[heap_count-1] == leonardo_numbers[heap_count-3] and 
             heap_sizes[heap_count-2] == leonardo_numbers[heap_count-4])):
            # Merge heaps
            heap_count -= 1
            heap_sizes[heap_count-1] += 1
        elif heap_count < 2 or heap_sizes[heap_count-1] != leonardo_numbers[heap_count-2] + 1:
            # Add new heap
            heap_sizes[heap_count] = 1
            heap_count += 1
        else:
            # Replace heap
            heap_count -= 1

        # Sift down to maintain heap property
        _sift_down(arr, heap_count - 1, heap_sizes[heap_count - 1])

    # Deheap and sort
    for i in range(len(arr) - 1, 0, -1):
        if heap_count > 0:
            # Remove largest element from heap
            heap_count -= 1
            
            # Sift down if needed
            if heap_count > 0:
                _sift_down(arr, 0, heap_sizes[heap_count - 1])

    return arr

def _sift_down(arr: List[T], heap_index: int, heap_size: int) -> None:
    """
    Sift down operation to maintain heap property.
    
    Args:
        arr (List[T]): The list being sorted.
        heap_index (int): Index of the current heap.
        heap_size (int): Size of the current heap.
    """
    r = heap_index
    child_heap_index = r + 1
    child_heap_size = 1

    # Find largest among root and its children
    while child_heap_index < len(arr):
        # Choose larger child
        if child_heap_index + child_heap_size < len(arr) and \
           arr[child_heap_index + child_heap_size] > arr[child_heap_index]:
            child_heap_index += child_heap_size
            child_heap_size += 1

        # Compare child with root
        if arr[child_heap_index] <= arr[r]:
            break

        # Swap
        arr[r], arr[child_heap_index] = arr[child_heap_index], arr[r]

        # Update indices
        r = child_heap_index
        child_heap_index = r + 1
        child_heap_size = 1