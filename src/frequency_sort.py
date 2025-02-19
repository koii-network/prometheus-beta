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
    
    # Create a stability-preserving sorted list
    def custom_sort_key(num):
        return (freq_count[num], nums.index(num))
    
    # Sort unique numbers by frequency and first occurrence
    freq_sorted_unique = sorted(set(nums), key=custom_sort_key)
    
    # Create the result list respecting both frequency and original order
    result = []
    for num in freq_sorted_unique:
        result.extend([num] * freq_count[num])
    
    return result