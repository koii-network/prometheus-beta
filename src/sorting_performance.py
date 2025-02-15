import time
import random
import logging
from typing import List, Callable, Dict, Any

def log_sorting_performance(
    algorithms: Dict[str, Callable[[List[int]], List[int]]],
    input_sizes: List[int],
    num_runs: int = 5
) -> Dict[str, Dict[str, float]]:
    """
    Compare and log performance of multiple sorting algorithms.

    Args:
        algorithms: Dictionary of sorting algorithms to compare
        input_sizes: List of input sizes to test
        num_runs: Number of runs for each input size to get average performance

    Returns:
        Performance metrics dictionary with average time and comparisons for each algorithm
    """
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    performance_results = {}

    for size in input_sizes:
        logger.info(f"Testing sorting algorithms with input size: {size}")
        performance_results[size] = {}

        for algo_name, sorting_func in algorithms.items():
            # Prepare running times and comparison counts
            run_times = []

            for _ in range(num_runs):
                # Generate random input list
                test_input = [random.randint(0, 1000) for _ in range(size)]
                
                # Measure time
                start_time = time.time()
                sorted_result = sorting_func(test_input.copy())
                end_time = time.time()

                # Calculate and store execution time
                run_times.append(end_time - start_time)

            # Calculate average time
            avg_time = sum(run_times) / num_runs
            performance_results[size][algo_name] = {
                'avg_time': avg_time,
                'runs': run_times
            }

            logger.info(f"{algo_name} - Avg Time for {size} elements: {avg_time:.6f} seconds")

    return performance_results

# Example sorting algorithms for demonstration
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)