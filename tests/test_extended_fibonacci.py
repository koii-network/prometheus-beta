import pytest
import math
from src.extended_fibonacci import extended_fibonacci

def test_basic_positive_indices():
    assert extended_fibonacci(0) == 0
    assert extended_fibonacci(1) == 1
    assert extended_fibonacci(2) == 1
    assert extended_fibonacci(3) == 2
    assert extended_fibonacci(4) == 3
    assert extended_fibonacci(5) == 5
    assert extended_fibonacci(6) == 8

def test_basic_negative_indices():
    assert extended_fibonacci(-1) == 1
    assert extended_fibonacci(-2) == -1
    assert extended_fibonacci(-3) == 2
    assert extended_fibonacci(-4) == -3
    assert extended_fibonacci(-5) == 5
    assert extended_fibonacci(-6) == -8

def test_floating_point_indices():
    # Test interpolation
    assert math.isclose(extended_fibonacci(2.5), 1.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(3.25), 1.75, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(-2.5), -1.5, rel_tol=1e-9)

def test_large_indices():
    # Test larger indices to ensure computational stability
    assert extended_fibonacci(10) == 55
    assert extended_fibonacci(-10) == 55
    assert extended_fibonacci(15) == 610
    assert extended_fibonacci(-15) == -610

def test_type_handling():
    with pytest.raises(TypeError):
        extended_fibonacci("invalid")
    with pytest.raises(TypeError):
        extended_fibonacci([1, 2, 3])

def test_complex_cases():
    # Check some precise floating-point interpolations
    assert math.isclose(extended_fibonacci(4.75), 5.75, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(-4.75), -5.75, rel_tol=1e-9)