import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort is a sorting algorithm that uses threading and sleep time 
    to sort numbers. Each number creates a thread that sleeps proportionally 
    to its value and then adds itself to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of numbers
    
    Raises:
        ValueError: If input list contains negative numbers
        TypeError: If input list contains non-numeric types
    """
    # Validate input
    if not arr:
        return []
    
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort does not support negative numbers")
    
    # Check for non-numeric types
    if not all(isinstance(num, (int, float)) for num in arr):
        raise TypeError("Input must be a list of numbers")
    
    # Thread-safe result list and lock
    result = []
    result_lock = threading.Lock()
    
    # Create threads for each number
    threads = []
    for num in arr:
        def worker(x):
            time.sleep(x * 0.001)  # Sleep proportional to number value
            with result_lock:
                result.append(x)
        
        t = threading.Thread(target=worker, args=(num,))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return result