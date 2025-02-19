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
    
    # Create a custom sorting key that considers:
    # 1. Frequency (ascending)
    # 2. First occurrence index
    def custom_sort_key(num):
        return (freq_count[num], nums.index(num))
    
    # Enumerate to maintain original order as secondary sort key
    enumerated_nums = list(enumerate(nums))
    
    # Sort based on frequency and first occurrence
    sorted_nums = sorted(
        enumerated_nums, 
        key=lambda x: (freq_count[x[1]], x[0])
    )
    
    # Extract only the numbers, maintaining the sorted order
    return [num for _, num in sorted_nums]