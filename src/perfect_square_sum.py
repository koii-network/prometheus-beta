from itertools import combinations, permutations
from math import sqrt

def sum_perfect_squares_from_set(integer_set):
    """
    Calculates the sum of all unique perfect squares that can be formed 
    from the integers in the given set.
    
    Args:
        integer_set (set): A set of integers
    
    Returns:
        int: Sum of all unique perfect squares formable from the set
    """
    # Validate input is a set of integers
    if not isinstance(integer_set, set):
        raise TypeError("Input must be a set")
    
    if not all(isinstance(x, int) for x in integer_set):
        raise TypeError("Set must contain only integers")
    
    # Find all possible perfect squares
    perfect_squares = set()
    
    # Convert set to sorted list
    numbers = sorted(list(integer_set))
    
    # Try all possible combinations and permutations
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            # Try all permutations of the combination
            for perm in permutations(combo):
                # Generate numbers from all possible ways of joining digits
                for i in range(1, len(perm) + 1):
                    subseqs = [''.join(map(str, perm[:i]))]
                    for j in range(1, len(perm) - i + 1):
                        subseqs.append(subseqs[-1] + ''.join(map(str, perm[i:i+j])))
                    
                    # Check each generated number
                    for subseq in subseqs:
                        # Skip leading zeros
                        if subseq.startswith('0'):
                            continue
                        
                        num = int(subseq)
                        
                        # Check if the number is a perfect square
                        if num > 0:
                            sqrt_val = int(sqrt(num))
                            if sqrt_val * sqrt_val == num:
                                perfect_squares.add(num)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)