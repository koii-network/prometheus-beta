import time
import random
import logging

def compare_sorting_algorithms(algorithm1, algorithm2, input_list):
    """
    Compare the performance of two sorting algorithms.
    
    Args:
        algorithm1 (callable): First sorting algorithm function
        algorithm2 (callable): Second sorting algorithm function
        input_list (list): List to be sorted
    
    Returns:
        dict: Performance comparison results
    """
    # Create a copy of the input list to ensure fair comparison
    list1 = input_list.copy()
    list2 = input_list.copy()
    
    # Measure performance of first algorithm
    start_time1 = time.time()
    algorithm1(list1)
    end_time1 = time.time()
    time1 = end_time1 - start_time1
    
    # Measure performance of second algorithm
    start_time2 = time.time()
    algorithm2(list2)
    end_time2 = time.time()
    time2 = end_time2 - start_time2
    
    # Logging performance results
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger(__name__)
    
    logger.info(f"Algorithm 1 Performance: {time1:.6f} seconds")
    logger.info(f"Algorithm 2 Performance: {time2:.6f} seconds")
    
    return {
        'algorithm1_time': time1,
        'algorithm2_time': time2,
        'faster_algorithm': algorithm1.__name__ if time1 < time2 else algorithm2.__name__
    }

# Example sorting algorithms for demonstration
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == '__main__':
    # Generate a random list for testing
    test_list = [random.randint(1, 1000) for _ in range(1000)]
    
    # Compare bubble sort and quick sort
    result = compare_sorting_algorithms(bubble_sort, quick_sort, test_list)
    print(result)