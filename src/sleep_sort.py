import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort is a sorting algorithm that creates a separate thread for each element,
    which sleeps for a time proportional to the value of the element before adding 
    it to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of numbers
    
    Raises:
        ValueError: If input list contains negative numbers
        TypeError: If input contains non-numeric types
    """
    # Validate input
    if not arr:
        return []
    
    # Validate input types first
    try:
        # Convert to float to catch any non-numeric types
        float_arr = [float(num) for num in arr]
    except (TypeError, ValueError):
        raise TypeError("Input must be a list of numbers")
    
    # Check for negative numbers
    if any(num < 0 for num in float_arr):
        raise ValueError("Sleep sort does not support negative numbers")
    
    # Thread-safe shared result list
    result = []
    lock = threading.Lock()
    
    # Create threads for each element
    threads = []
    for num in float_arr:
        def worker(x):
            time.sleep(x / 100.0)  # Proportional sleep time
            with lock:
                result.append(x)
        
        thread = threading.Thread(target=worker, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result