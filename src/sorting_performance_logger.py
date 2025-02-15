import time
import random
import statistics
from typing import List, Callable, Dict, Any

def log_sorting_performance(
    algorithms: Dict[str, Callable[[List[int]], List[int]]],
    input_generator: Callable[[int], List[int]] = lambda n: [random.randint(1, 1000) for _ in range(n)],
    input_sizes: List[int] = [100, 1000, 10000],
    num_runs: int = 5
) -> Dict[str, Dict[str, float]]:
    """
    Compare performance of multiple sorting algorithms across different input sizes.
    
    Args:
        algorithms (Dict[str, Callable]): Dictionary of sorting algorithms to compare
        input_generator (Callable): Function to generate input lists (default: random integers)
        input_sizes (List[int]): Different input sizes to test
        num_runs (int): Number of runs for each algorithm and input size
    
    Returns:
        Dict containing performance metrics for each algorithm
    """
    performance_results = {}
    
    for size in input_sizes:
        performance_results[size] = {}
        
        for algo_name, sorting_func in algorithms.items():
            # Store execution times for this algorithm and input size
            execution_times = []
            
            for _ in range(num_runs):
                # Generate input list
                input_list = input_generator(size)
                
                # Create a copy to avoid modifying the original list
                test_list = input_list.copy()
                
                # Measure sorting time
                start_time = time.perf_counter()
                sorted_list = sorting_func(test_list)
                end_time = time.perf_counter()
                
                # Calculate and store execution time
                execution_time = end_time - start_time
                execution_times.append(execution_time)
            
            # Calculate statistics for this algorithm
            performance_results[size][algo_name] = {
                'mean_time': statistics.mean(execution_times),
                'median_time': statistics.median(execution_times),
                'min_time': min(execution_times),
                'max_time': max(execution_times),
                'std_dev': statistics.stdev(execution_times) if len(execution_times) > 1 else 0
            }
    
    return performance_results