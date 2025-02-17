import os
import pytest
import tempfile
import mock
from src.file_permissions import change_file_permissions

def test_change_file_permissions():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Initially set read-only permissions
        os.chmod(temp_path, 0o444)
        
        # Change permissions to read-write
        result = change_file_permissions(temp_path, 0o666)
        assert result is True
        
        # Verify permissions changed
        current_mode = os.stat(temp_path).st_mode
        assert (current_mode & 0o777) == 0o666
    finally:
        # Clean up temporary file
        os.unlink(temp_path)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('non_existent_file.txt', 0o755)

def test_invalid_file_path():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)

def test_invalid_mode():
    # Mocking os.path.exists to simulate file existence for mode validation
    with mock.patch('os.path.exists', return_value=True), \
         mock.patch('os.chmod', return_value=None):
        with pytest.raises(TypeError):
            change_file_permissions('some_file.txt', '755')
        
        with pytest.raises(ValueError):
            change_file_permissions('some_file.txt', 0o1000)  # Out of valid range