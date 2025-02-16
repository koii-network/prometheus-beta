import os
import pytest
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions_success(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Initial permissions (readable and writable by owner)
    initial_mode = 0o600
    os.chmod(test_file, initial_mode)
    
    # Change permissions to be executable too
    new_mode = 0o700
    result = change_file_permissions(str(test_file), new_mode)
    
    # Check return value
    assert result is True
    
    # Check actual file permissions
    current_mode = stat.S_IMODE(os.stat(test_file).st_mode)
    assert current_mode == new_mode

def test_change_file_permissions_invalid_path():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/path/to/nonexistent/file.txt", 0o755)

def test_change_file_permissions_invalid_type():
    with pytest.raises(TypeError):
        change_file_permissions(123, "invalid")
    
    with pytest.raises(TypeError):
        change_file_permissions("/path/to/file", "invalid")

def test_change_file_permissions_different_modes(tmp_path):
    test_file = tmp_path / "test_permission_file.txt"
    test_file.write_text("Test content")
    
    # Test multiple permission modes
    modes = [0o644, 0o755, 0o600, 0o777]
    
    for mode in modes:
        result = change_file_permissions(str(test_file), mode)
        assert result is True
        
        current_mode = stat.S_IMODE(os.stat(test_file).st_mode)
        assert current_mode == mode