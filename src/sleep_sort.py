import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number,
    where each thread sleeps for a duration proportional to the number,
    and then adds the number to the result list.
    
    Args:
        arr (List[int]): Input list of positive integers to be sorted.
    
    Returns:
        List[int]: Sorted list of integers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Validate input
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # If input is empty, return empty list
    if not arr:
        return []
    
    # Determine maximum value for scaling and timing
    max_val = max(arr)
    
    # Create synchronization primitives
    result = []
    result_lock = threading.Lock()
    sorting_complete = threading.Event()
    
    # Create threads for each number
    def insert(num, index):
        # Scale sleep time and add a small correction for order stability
        scale_factor = 0.001
        correction = index * 0.0001  # Add a small correction based on original index
        time.sleep(num * scale_factor + correction)
        
        with result_lock:
            result.append(num)
        
        # If this is the last thread, signal completion
        if num == max_val:
            sorting_complete.set()
    
    # Create and start threads
    threads = []
    for i, num in enumerate(arr):
        thread = threading.Thread(target=insert, args=(num, i))
        thread.start()
        threads.append(thread)
    
    # Wait for sorting to complete
    sorting_complete.wait()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result