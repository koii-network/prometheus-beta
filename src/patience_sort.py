from typing import List, TypeVar, Union
import heapq

# Define a generic type that supports comparison
T = TypeVar('T', bound=Union[int, float, str])

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort works by creating piles of sorted elements, 
    similar to the card game Patience (Solitaire). It has a time complexity of O(n log n).
    
    Args:
        arr (List[T]): Input list to be sorted
    
    Returns:
        List[T]: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list or contains incomparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles
    piles = []
    
    # Distribute elements into piles
    for item in arr:
        # Binary search to find the right pile
        left, right = 0, len(piles)
        while left < right:
            mid = (left + right) // 2
            if piles[mid][-1] <= item:
                left = mid + 1
            else:
                right = mid
        
        # If found a suitable pile, append to that pile
        if left < len(piles):
            piles[left].append(item)
        # Otherwise, create a new pile
        else:
            piles.append([item])
    
    # Use a min-heap to merge piles
    heap = [(pile[0], i, 0) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    # Reconstruct sorted list
    result = []
    while heap:
        val, pile_index, element_index = heapq.heappop(heap)
        result.append(val)
        
        # Move to next element in the pile
        element_index += 1
        if element_index < len(piles[pile_index]):
            next_val = piles[pile_index][element_index]
            heapq.heappush(heap, (next_val, pile_index, element_index))
    
    return result