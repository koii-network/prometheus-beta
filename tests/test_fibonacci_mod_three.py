import pytest
from src.fibonacci_mod_three import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic sequence generation."""
    assert generate_modified_fibonacci(1) == [1]
    assert generate_modified_fibonacci(2) == [1, 1]
    assert generate_modified_fibonacci(3) == [1, 1, 2]
    assert generate_modified_fibonacci(4) == [1, 1, 2, 3]
    assert generate_modified_fibonacci(5) == [1, 1, 2, 3, 5]

def test_divisibility_constraint():
    """Verify the divisibility constraint for the sequence."""
    def is_sum_divisible_by_three(seq):
        """Check if sum of consecutive numbers is divisible by 3 from 3rd element onward."""
        if len(seq) < 3:
            return True
        return all((seq[i-2] + seq[i-1]) % 3 == 0 for i in range(2, len(seq)))
    
    # Test various sequence lengths
    test_cases = [1, 2, 3, 4, 5, 10, 15]
    for n in test_cases:
        seq = generate_modified_fibonacci(n)
        assert is_sum_divisible_by_three(seq), f"Failed for n={n}, sequence: {seq}"

def test_input_validation():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci("not a number")