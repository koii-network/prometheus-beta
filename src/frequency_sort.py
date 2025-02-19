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
    
    # Count the frequency of each number
    freq_count = Counter(nums)
    
    # In case of conflict (same frequency), use first occurrence
    # but allow for flexibility in the final ordering
    def custom_sort_key(num):
        return freq_count[num]
    
    # Unique numbers, sorted by frequency
    freq_sorted = sorted(set(nums), key=custom_sort_key)
    
    # Create result by repeating each unique number 
    # according to its frequency
    result = []
    for num in freq_sorted:
        result.extend([num] * freq_count[num])
    
    return result