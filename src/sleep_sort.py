import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort works by creating a separate thread for each number, 
    where each thread sleeps for a duration proportional to the number's value 
    before adding the number to the result list.
    
    Args:
        arr (List[int]): A list of positive integers to be sorted.
    
    Returns:
        List[int]: A sorted list of the input numbers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Validate input: reject negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort does not support negative numbers")
    
    # If input is empty, return empty list
    if not arr:
        return []
    
    # Shared list to collect sorted results
    result = []
    
    # Synchronization primitive to coordinate threads
    result_lock = threading.Lock()
    
    # Function to be run by each thread
    def sort_thread(num):
        # Sleep proportional to the number 
        # Use a small scaling factor to prevent extremely long waits
        time.sleep(num * 0.001)
        
        # Safely append to shared result list
        with result_lock:
            result.append(num)
    
    # Create and start a thread for each number
    threads = []
    for num in arr:
        thread = threading.Thread(target=sort_thread, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result