import time
import random
import typing

def compare_sorting_algorithms(
    algorithm1: typing.Callable[[list], list], 
    algorithm2: typing.Callable[[list], list], 
    input_sizes: list[int] = [100, 1000, 10000]
) -> list[dict]:
    """
    Compare performance of two sorting algorithms across different input sizes.
    
    Args:
        algorithm1 (callable): First sorting algorithm to compare
        algorithm2 (callable): Second sorting algorithm to compare
        input_sizes (list): List of input sizes to test
    
    Returns:
        list of dictionaries containing performance metrics
    """
    results = []
    
    for size in input_sizes:
        # Generate random list for testing
        test_list = [random.randint(0, 10000) for _ in range(size)]
        
        # Performance test for algorithm1
        test_list1 = test_list.copy()
        start_time1 = time.time()
        algorithm1(test_list1)
        time1 = time.time() - start_time1
        
        # Performance test for algorithm2
        test_list2 = test_list.copy()
        start_time2 = time.time()
        algorithm2(test_list2)
        time2 = time.time() - start_time2
        
        # Store results
        results.append({
            'input_size': size,
            'algorithm1_time': time1,
            'algorithm2_time': time2,
            'faster_algorithm': 'algorithm1' if time1 < time2 else 'algorithm2'
        })
    
    return results