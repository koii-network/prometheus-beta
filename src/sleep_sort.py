import threading
import time

def sleep_sort(arr):
    """
    Implement the sleep sort algorithm.
    
    Args:
        arr (list): A list of positive numbers to be sorted.
    
    Returns:
        list: A sorted list of input numbers.
    
    Raises:
        ValueError: If the input contains non-positive numbers.
    """
    # Check for non-positive numbers
    if any(num <= 0 for num in arr):
        raise ValueError("Sleep sort only works with positive numbers")
    
    # Create a shared list to store results
    result = []
    
    # Threading lock to ensure thread-safe appending
    lock = threading.Lock()
    
    # Function to sleep and append
    def sleep_and_append(num):
        time.sleep(num * 0.1)  # Scaled sleep time
        with lock:
            result.append(num)
    
    # Create and start threads for each number
    threads = []
    for num in arr:
        thread = threading.Thread(target=sleep_and_append, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result