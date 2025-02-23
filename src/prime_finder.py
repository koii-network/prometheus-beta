def find_primes(a: int, b: int) -> list[int]:
    """
    Find all prime numbers within the given range (inclusive).

    Args:
        a (int): Lower bound of the range
        b (int): Upper bound of the range

    Returns:
        list[int]: A list of prime numbers within the range [a, b]

    Raises:
        ValueError: If a or b is negative or a > b
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Input range must be non-negative")
    if a > b:
        raise ValueError("Lower bound must be less than or equal to upper bound")

    # Handle empty or trivial ranges
    if a > b:
        return []

    # Sieve of Eratosthenes algorithm for finding primes
    # Create a boolean array "is_prime[0..b]" and initialize 
    # all entries it as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (b + 1)
    is_prime[0] = is_prime[1] = False

    # Use Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(b**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, b+1, i):
                is_prime[j] = False

    # Collect primes in the specified range
    return [num for num in range(max(2, a), b+1) if is_prime[num]]