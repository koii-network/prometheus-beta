import pytest
import string
from src.password_generator import generate_password

def test_password_length():
    """Test that generated password matches specified length."""
    for length in [1, 5, 10, 20, 50]:
        password = generate_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that password contains characters from different sets."""
    password = generate_password(20)
    
    # Check that the password contains at least one character from each set
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_invalid_length_inputs():
    """Test error handling for invalid length inputs."""
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_password(-5)

def test_type_inputs():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_password("10")
    
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_password(3.14)
    
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_password(None)

def test_password_randomness():
    """Test that two generated passwords are not the same."""
    length = 20
    password1 = generate_password(length)
    password2 = generate_password(length)
    
    assert password1 != password2  # This is a probabilistic test