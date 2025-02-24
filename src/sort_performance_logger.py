import time
import random
import typing

def compare_sorting_algorithms(
    algorithm1: typing.Callable[[list], list], 
    algorithm2: typing.Callable[[list], list], 
    input_data: list, 
    num_iterations: int = 5
) -> dict:
    """
    Compare performance of two sorting algorithms.
    
    Args:
        algorithm1 (callable): First sorting algorithm to compare
        algorithm2 (callable): Second sorting algorithm to compare
        input_data (list): Input list to be sorted
        num_iterations (int): Number of times to run each algorithm for averaging
    
    Returns:
        dict: Performance comparison metrics
    """
    def measure_performance(algorithm, data):
        times = []
        for _ in range(num_iterations):
            # Create a copy to ensure fair comparison
            test_data = data.copy()
            
            start_time = time.perf_counter()
            algorithm(test_data)
            end_time = time.perf_counter()
            
            times.append(end_time - start_time)
        
        return {
            'avg_time': sum(times) / num_iterations,
            'min_time': min(times),
            'max_time': max(times)
        }
    
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Measure performance for both algorithms
    algo1_results = measure_performance(algorithm1, input_data)
    algo2_results = measure_performance(algorithm2, input_data)
    
    return {
        'algorithm1': {
            'name': algorithm1.__name__,
            **algo1_results
        },
        'algorithm2': {
            'name': algorithm2.__name__,
            **algo2_results
        },
        'faster_algorithm': algorithm1.__name__ if algo1_results['avg_time'] < algo2_results['avg_time'] else algorithm2.__name__
    }