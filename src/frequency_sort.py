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
    
    # Create a custom sorting key:
    # 1. Primary sort by frequency (ascending)
    # 2. Secondary sort by first occurrence
    def custom_key(num):
        return (freq_count[num], nums.index(num))
    
    # Sort the unique elements first
    unique_sorted = sorted(set(nums), key=custom_key)
    
    # Prepare the result list
    result = []
    for num in unique_sorted:
        # Find indices of this number in the original list
        indices = [i for i, x in enumerate(nums) if x == num]
        
        # Add all occurrences of the current number
        result.extend([num] * freq_count[num])
    
    return result