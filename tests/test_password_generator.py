import pytest
import string
from src.password_generator import generate_random_password

def test_password_length():
    """Test that the generated password matches the specified length."""
    lengths = [1, 5, 10, 20, 50]
    for length in lengths:
        password = generate_random_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that the generated password contains a mix of character types."""
    password = generate_random_password(20)
    
    # Check that the password contains at least one of each character type
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_randomness():
    """Test that multiple generated passwords are not identical."""
    passwords = {generate_random_password(10) for _ in range(100)}
    assert len(passwords) > 1

def test_invalid_length():
    """Test that an error is raised for invalid password length."""
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(-5)