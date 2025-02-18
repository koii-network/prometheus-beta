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
    
    # Create synchronization primitives
    result = []
    result_lock = threading.Lock()
    sorting_complete = threading.Event()
    
    # Create threads for each number
    def insert(num):
        time.sleep(num * 0.001)  # Sleep proportional to the number
        with result_lock:
            result.append(num)
        
        # If this is the last (largest) number, signal completion
        if num == max(arr):
            sorting_complete.set()
    
    # Create and start threads
    threads = []
    for num in arr:
        thread = threading.Thread(target=insert, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for sorting to complete
    sorting_complete.wait()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result