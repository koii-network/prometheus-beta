import pytest
import string
from src.password_generator import generate_random_password

def test_generate_random_password_length():
    """Test that the generated password matches the specified length."""
    for length in [8, 12, 16, 24]:
        password = generate_random_password(length)
        assert len(password) == length

def test_generate_random_password_characters():
    """Test that the password contains characters from different sets."""
    password = generate_random_password(12)
    
    # Check if password contains at least one character from each set
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_generate_random_password_randomness():
    """Test that multiple generated passwords are not identical."""
    passwords = set(generate_random_password(12) for _ in range(100))
    assert len(passwords) > 1

def test_generate_random_password_minimum_length():
    """Test that the function raises an error for invalid lengths."""
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_random_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_random_password(-5)

def test_generate_random_password_very_short():
    """Test password generation for the minimum valid length."""
    password = generate_random_password(1)
    assert len(password) == 1