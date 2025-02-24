import time
import random
import typing

def compare_sorting_algorithms(
    algorithm1: typing.Callable[[list], list], 
    algorithm2: typing.Callable[[list], list], 
    input_sizes: list[int] = [100, 1000, 10000],
    num_runs: int = 5
) -> dict:
    """
    Compare the performance of two sorting algorithms across different input sizes.
    
    Args:
        algorithm1 (callable): First sorting algorithm to compare
        algorithm2 (callable): Second sorting algorithm to compare
        input_sizes (list): List of input sizes to test
        num_runs (int): Number of runs for each input size to average performance
    
    Returns:
        dict: Performance comparison results
    """
    results = {
        'algorithm1_name': algorithm1.__name__,
        'algorithm2_name': algorithm2.__name__,
        'performance_comparison': []
    }
    
    for size in input_sizes:
        # Prepare performance tracking for this input size
        algo1_times = []
        algo2_times = []
        
        for _ in range(num_runs):
            # Generate random list for fair comparison
            original_list = [random.randint(0, 10000) for _ in range(size)]
            
            # Test algorithm 1
            test_list1 = original_list.copy()
            start_time = time.time()
            algorithm1(test_list1)
            algo1_time = time.time() - start_time
            algo1_times.append(algo1_time)
            
            # Test algorithm 2
            test_list2 = original_list.copy()
            start_time = time.time()
            algorithm2(test_list2)
            algo2_time = time.time() - start_time
            algo2_times.append(algo2_time)
        
        # Calculate average times
        avg_algo1_time = sum(algo1_times) / num_runs
        avg_algo2_time = sum(algo2_times) / num_runs
        
        results['performance_comparison'].append({
            'input_size': size,
            f'{algorithm1.__name__}_avg_time': avg_algo1_time,
            f'{algorithm2.__name__}_avg_time': avg_algo2_time,
            'faster_algorithm': algorithm1.__name__ if avg_algo1_time < avg_algo2_time else algorithm2.__name__
        })
    
    return results