import pytest
from src.fibonacci import fibonacci_log_time

def test_fibonacci_log_time_basic_cases():
    """Test basic Fibonacci number calculations."""
    assert fibonacci_log_time(0) == 0
    assert fibonacci_log_time(1) == 1
    assert fibonacci_log_time(2) == 1
    assert fibonacci_log_time(3) == 2
    assert fibonacci_log_time(4) == 3
    assert fibonacci_log_time(5) == 5
    assert fibonacci_log_time(6) == 8
    assert fibonacci_log_time(7) == 13

def test_fibonacci_log_time_larger_numbers():
    """Test Fibonacci numbers for larger indices."""
    assert fibonacci_log_time(10) == 55
    assert fibonacci_log_time(20) == 6765
    assert fibonacci_log_time(30) == 832040

def test_fibonacci_log_time_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-1)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-100)

def test_fibonacci_log_time_performance():
    """Verify that the function can handle large inputs quickly."""
    # These numbers would be extremely slow with recursive or naive approaches
    assert fibonacci_log_time(100) == 354224848179261915075
    assert fibonacci_log_time(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875