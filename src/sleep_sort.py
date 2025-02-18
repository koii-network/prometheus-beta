import threading
import time

def sleep_sort(arr):
    """
    Implement the sleep sort algorithm.
    
    This algorithm works by creating a separate thread for each number,
    where each thread sleeps for a duration proportional to its input value 
    and then adds the value to the result list.
    
    Args:
        arr (list): A list of positive integers to be sorted.
    
    Returns:
        list: A sorted list of input numbers.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input contains non-integer values.
    """
    # Validate input
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Negative numbers are not supported")
    
    # Create a list to store results and a lock for thread-safe appending
    results = []
    results_lock = threading.Lock()
    
    # Function to be run by each thread
    def sort_thread(num):
        # Sleep proportional to the number's value
        time.sleep(num * 0.001)  # Small multiplier to make sorting work
        
        # Thread-safe append to results
        with results_lock:
            results.append(num)
    
    # Create and start threads for each number
    threads = []
    for num in arr:
        t = threading.Thread(target=sort_thread, args=(num,))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return results