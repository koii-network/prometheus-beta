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
    
    # Prepare synchronization primitives
    result = []
    result_lock = threading.Lock()
    barrier = threading.Barrier(len(arr) + 1)
    
    # Create threads for each number
    def insert(num):
        # Sleep proportional to the number
        time.sleep(num * 0.001)
        
        # Synchronize threads
        barrier.wait()
        
        # Add to result
        with result_lock:
            result.append(num)
    
    # Create and start threads
    threads = []
    for num in arr:
        thread = threading.Thread(target=insert, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to be ready
    barrier.wait()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return sorted(result)