import pytest
import string
from src.password_generator import generate_random_password

def test_password_length():
    """Test that generated password matches the specified length."""
    for length in [1, 5, 10, 20, 50]:
        password = generate_random_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that the password contains characters from different sets."""
    password = generate_random_password(20)
    
    # Check that password contains at least one character from each set
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_invalid_length_inputs():
    """Test error handling for invalid length inputs."""
    # Test negative length
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(-1)
    
    # Test zero length
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(0)

def test_invalid_type_inputs():
    """Test error handling for invalid input types."""
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password("10")
    
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password(3.14)
    
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password(None)

def test_randomness():
    """Verify that multiple generated passwords are different."""
    passwords = set()
    for _ in range(100):
        password = generate_random_password(10)
        passwords.add(password)
    
    # With 100 generations, it's extremely unlikely to have all the same password
    assert len(passwords) > 1