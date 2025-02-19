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
    
    # Track first occurrences to use as secondary sorting key
    first_occurrences = {num: nums.index(num) for num in freq_count}
    
    # Create a list of unique numbers sorted by their frequency and first occurrence
    unique_nums = sorted(
        freq_count.keys(), 
        key=lambda x: (freq_count[x], first_occurrences[x])
    )
    
    # Construct the result by expanding the unique numbers 
    # according to their frequency in the order determined above
    result = []
    for num in unique_nums:
        result.extend([num] * freq_count[num])
    
    return result