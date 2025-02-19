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
    
    # Preserve original indices for stable sorting
    enumerated_nums = list(enumerate(nums))
    
    # Create a custom sorting key:
    # 1. Primary sort by frequency (ascending)
    # 2. Secondary sort by original index of first occurrence
    def custom_sort_key(item):
        index, num = item
        return (freq_count[num], index)
    
    # Sort, then extract only the numbers
    return [num for _, num in sorted(enumerated_nums, key=custom_sort_key)]