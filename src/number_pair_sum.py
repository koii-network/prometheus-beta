def sum_pairs_with_nine_diff(file_path):
    """
    Read numbers from a text file and return the sum of pairs with a difference of 9.

    Args:
        file_path (str): Path to the text file containing numbers.

    Returns:
        int: Sum of all pairs of numbers with a difference of 9.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file contains non-numeric values.
    """
    try:
        # Read numbers from the file
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric values")

    # Find pairs with difference of 9 and sum them
    pair_sum = 0
    used_numbers = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Check the difference exactly 9 in either direction
            if abs(numbers[i] - numbers[j]) == 9:
                # Check if both numbers are unique
                if numbers[i] not in used_numbers and numbers[j] not in used_numbers:
                    pair_sum += numbers[i] + numbers[j]
                    used_numbers.add(numbers[i])
                    used_numbers.add(numbers[j])

    return pair_sum