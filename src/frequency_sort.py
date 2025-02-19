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
    
    # Sort unique numbers by frequency, prioritizing first occurrence
    freq_sorted_unique = sorted(
        set(nums), 
        key=lambda x: (freq_count[x], nums.index(x))
    )
    
    # Create result by repeating numbers according to their frequency
    return [num for num in freq_sorted_unique for _ in range(freq_count[num])]