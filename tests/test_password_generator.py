import pytest
import string
from src.password_generator import generate_random_password

def test_password_length():
    """Test that generated password matches the specified length."""
    for length in [8, 12, 16, 24]:
        password = generate_random_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that generated password includes characters from all character sets."""
    password = generate_random_password(12)
    
    assert any(char in string.ascii_lowercase for char in password), "Missing lowercase"
    assert any(char in string.ascii_uppercase for char in password), "Missing uppercase"
    assert any(char in string.digits for char in password), "Missing digits"
    assert any(char in string.punctuation for char in password), "Missing punctuation"

def test_password_randomness():
    """Test that multiple generated passwords are different."""
    passwords = set(generate_random_password(12) for _ in range(100))
    assert len(passwords) > 1, "Generated passwords are not sufficiently random"

def test_invalid_length_too_short():
    """Test that an error is raised for password length less than 4."""
    with pytest.raises(ValueError, match="Password length must be at least 4 characters"):
        generate_random_password(3)

def test_invalid_length_type():
    """Test that an error is raised for non-integer length."""
    with pytest.raises(TypeError, match="Length must be an integer"):
        generate_random_password("not an integer")