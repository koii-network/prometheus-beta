import pytest
from src.verification_code import generate_verification_code, validate_verification_code

def test_generate_verification_code():
    """Test that generate_verification_code returns a valid 6-digit code."""
    code = generate_verification_code()
    assert validate_verification_code(code), "Generated code should be valid"
    assert len(code) == 6, "Code should be 6 digits long"

def test_generate_unique_codes():
    """Test that generate_verification_code creates unique codes."""
    used_codes = set()
    num_codes = 50
    
    for _ in range(num_codes):
        code = generate_verification_code(used_codes)
        assert code not in used_codes, f"Code {code} should be unique"
        used_codes.add(code)
    
    assert len(used_codes) == num_codes, "All generated codes should be unique"

def test_generate_code_with_existing_codes():
    """Test generating a code with existing codes in the set."""
    used_codes = {"123456", "654321"}
    code = generate_verification_code(used_codes)
    
    assert code not in used_codes, "Generated code should not be in existing codes"
    assert validate_verification_code(code), "Generated code should be valid"

def test_validation_function():
    """Test various scenarios for validate_verification_code."""
    # Valid codes
    assert validate_verification_code("123456") == True
    assert validate_verification_code("000000") == True
    assert validate_verification_code("999999") == True
    
    # Invalid codes
    assert validate_verification_code("12345") == False  # Too short
    assert validate_verification_code("1234567") == False  # Too long
    assert validate_verification_code("12345a") == False  # Contains non-digit
    assert validate_verification_code(123456) == False  # Not a string
    assert validate_verification_code("") == False  # Empty string

def test_generate_code_exhaustion():
    """Test that an error is raised when unique codes cannot be generated."""
    used_codes = set(f"{i:06d}" for i in range(1000000))
    
    with pytest.raises(ValueError, match="Unable to generate a unique verification code"):
        generate_verification_code(used_codes)