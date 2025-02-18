import pytest
import string
from src.password_generator import generate_random_password

def test_password_length():
    """Test that the generated password matches the specified length."""
    for length in [8, 12, 16, 24]:
        password = generate_random_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that the generated password includes different character types."""
    password = generate_random_password(12)
    
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_invalid_length():
    """Test that an error is raised for invalid password length."""
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_random_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_random_password(-5)

def test_password_randomness():
    """Test that multiple generated passwords are not the same."""
    passwords = set(generate_random_password(12) for _ in range(100))
    assert len(passwords) > 1  # Very high probability of different passwords