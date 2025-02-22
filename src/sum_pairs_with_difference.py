def sum_pairs_with_difference_nine(file_path):
    """
    Read numbers from a text file and return the sum of all pairs 
    that have a difference of 9.
    
    Args:
        file_path (str): Path to the text file containing numbers
    
    Returns:
        int: Sum of pairs with a difference of 9
    
    Raises:
        FileNotFoundError: If the file cannot be found
        ValueError: If the file contains non-numeric content
    """
    try:
        # Read numbers from the file
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        
        # Find pairs with difference of 9 and sum them
        pair_sum = 0
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if abs(numbers[i] - numbers[j]) == 9:
                    pair_sum += numbers[i] + numbers[j]
        
        return pair_sum
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric content")