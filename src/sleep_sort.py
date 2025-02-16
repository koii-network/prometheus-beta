import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Args:
        arr (List[int]): A list of positive integers to be sorted.
    
    Returns:
        List[int]: Sorted list of input integers.
    
    Raises:
        ValueError: If any number in the input is negative.
    """
    # Validate input
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # Result list to store sorted numbers
    result = []
    
    # Synchronization primitive to ensure thread-safe result appending
    result_lock = threading.Lock()
    
    # Create a thread for each number
    threads = []
    for num in arr:
        def worker(x):
            # Sleep proportional to the number
            time.sleep(x * 0.001)  # Small multiplier to keep sorting reasonable
            with result_lock:
                result.append(x)
        
        thread = threading.Thread(target=worker, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result