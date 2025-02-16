import pytest
import string
from src.password_generator import generate_random_password

def test_generate_random_password_length():
    """Test that the password generation works for various lengths."""
    lengths = [1, 5, 10, 20, 50]
    for length in lengths:
        password = generate_random_password(length)
        assert len(password) == length

def test_generate_random_password_characters():
    """Test that the password contains characters from expected sets."""
    password = generate_random_password(20)
    
    # Check that the password contains at least one character from each set
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_generate_random_password_randomness():
    """Test that different passwords are generated each time."""
    passwords = set(generate_random_password(10) for _ in range(100))
    assert len(passwords) > 1  # Highly unlikely to generate the same password multiple times

def test_generate_random_password_invalid_length():
    """Test that an error is raised for invalid password lengths."""
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(-5)