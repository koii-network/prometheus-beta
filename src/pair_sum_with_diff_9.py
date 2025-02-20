def sum_pairs_with_diff_9(file_path):
    """
    Read numbers from a text file and return the sum of all pairs with a difference of 9.
    
    Args:
        file_path (str): Path to the text file containing numbers
    
    Returns:
        int: Sum of all pairs of numbers with a difference of 9
    
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file contains non-numeric values
    """
    try:
        with open(file_path, 'r') as file:
            # Read and convert numbers, handling potential whitespace
            numbers = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric values")
    
    # Track the sum of pairs
    pair_sum = 0
    
    # Use a set for O(n) time complexity
    seen_numbers = set()
    
    for num in numbers:
        # Check if the complement (num+9 or num-9) exists
        if num + 9 in seen_numbers:
            pair_sum += num + (num + 9)
        if num - 9 in seen_numbers:
            pair_sum += num + (num - 9)
        
        # Add current number to seen numbers
        seen_numbers.add(num)
    
    return pair_sum