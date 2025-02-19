from collections import Counter
from typing import List

def frequency_sort(nums: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency, with less frequent 
    elements appearing first and more frequent elements appearing later.
    
    Args:
        nums (List[int]): Input list of integers
    
    Returns:
        List[int]: Sorted list based on frequency and original value
    """
    # Count the frequency of each number
    freq_count = Counter(nums)
    
    # Sort the list based on two criteria:
    # 1. Frequency (ascending)
    # 2. Original value (for numbers with same frequency)
    return sorted(nums, key=lambda x: (freq_count[x], x))