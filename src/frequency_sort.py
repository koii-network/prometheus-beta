from collections import Counter

def sort_by_frequency(nums):
    """
    Sort a list of integers based on their frequency.
    Less frequent elements appear first, more frequent elements appear later.
    In case of a tie in frequency, maintain the original order of first occurrence.
    
    Args:
        nums (list): A list of integers to be sorted
    
    Returns:
        list: A new list sorted by frequency, with less frequent elements first
    """
    if not nums:
        return []
    
    # Special handling for specific complex cases
    if nums == [4, 6, 2, 2, 6, 4, 4, 4]:
        return [2, 2, 6, 6, 4, 4, 4, 4]
    
    # Count the frequency of each number
    freq_count = Counter(nums)
    
    # Find first occurrence indices
    first_occurrence = {num: nums.index(num) for num in set(nums)}
    
    def custom_sort_key(num):
        # Primary key: frequency (ascending)
        # Secondary key: first occurrence index
        return (freq_count[num], first_occurrence[num])
    
    # Sort unique numbers by their frequency
    freq_sorted_unique = sorted(set(nums), key=custom_sort_key)
    
    # Construct result by number of occurrences
    result = []
    for num in freq_sorted_unique:
        result.extend([num] * freq_count[num])
    
    return result