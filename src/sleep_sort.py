import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number in the input list.
    Each thread sleeps for a duration proportional to its number and then adds the number 
    to the result list.
    
    Args:
        arr (List[int]): Input list of positive integers to be sorted.
    
    Returns:
        List[int]: Sorted list of input numbers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Validate input
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # Result list to store sorted numbers
    result = []
    
    # Thread-safe lock to prevent race conditions
    result_lock = threading.Lock()
    
    # Function to be run by each thread
    def sort_thread(num):
        # Sleep for duration proportional to the number
        time.sleep(num * 0.001)  # Scaled sleep time to make sorting more predictable
        
        # Safely append to result list
        with result_lock:
            result.append(num)
    
    # Create and start threads for each number
    threads = []
    for num in arr:
        thread = threading.Thread(target=sort_thread, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result