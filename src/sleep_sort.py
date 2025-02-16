import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number,
    where each thread sleeps for a duration proportional to the number's value,
    and then adds the number to the result list.
    
    Args:
        arr (List[int]): A list of positive integers to be sorted.
    
    Returns:
        List[int]: A sorted list of input numbers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # Create a thread-safe output list
    result = []
    lock = threading.Lock()
    
    # Create a thread for each number
    threads = []
    for num in arr:
        def worker(n):
            time.sleep(n * 0.001)  # Sleep proportional to the number
            with lock:
                result.append(n)
        
        thread = threading.Thread(target=worker, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result