import os
import pytest
import tempfile
from src.file_permissions import change_file_permissions

def test_change_file_permissions_valid():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Initial check: default permissions
    initial_mode = os.stat(temp_path).st_mode
    
    try:
        # Try changing permissions
        result = change_file_permissions(temp_path, 0o777)
        assert result is True
        
        # Verify mode changed
        new_mode = os.stat(temp_path).st_mode
        assert new_mode & 0o777 == 0o777
    finally:
        # Clean up: remove temp file
        os.unlink(temp_path)

def test_change_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('nonexistent_file.txt', 0o644)

def test_change_file_permissions_invalid_type_path():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o644)

def test_change_file_permissions_invalid_type_mode():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        with pytest.raises(TypeError):
            change_file_permissions(temp_path, '644')
    finally:
        os.unlink(temp_path)

def test_change_file_permissions_various_modes():
    modes_to_test = [0o644, 0o755, 0o600, 0o700]
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        for mode in modes_to_test:
            change_file_permissions(temp_path, mode)
            new_mode = os.stat(temp_path).st_mode
            assert new_mode & 0o777 == mode
    finally:
        os.unlink(temp_path)