from collections import Counter

def sort_by_frequency(nums):
    """
    Sort a list of integers based on their frequency.
    Less frequent elements appear first, more frequent elements appear later.
    If two elements have the same frequency, maintain their relative original order.
    
    Args:
        nums (list): A list of integers to be sorted
    
    Returns:
        list: Sorted list based on frequency (ascending)
    """
    # Count the frequency of each number
    freq_counter = Counter(nums)
    
    # Use a stable sort with key being the frequency
    # The stable sort ensures original order is maintained for equal frequencies
    return sorted(nums, key=lambda x: freq_counter[x])