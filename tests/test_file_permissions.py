import os
import pytest
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions_success(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Initial permissions (default usually 0o644)
    initial_mode = test_file.stat().st_mode
    
    # Change permissions to read-only
    result = change_file_permissions(str(test_file), 0o444)
    assert result is True
    
    # Check new permissions
    new_mode = test_file.stat().st_mode
    assert stat.S_IMODE(new_mode) == 0o444
    assert not os.access(str(test_file), os.W_OK)

def test_change_file_permissions_full_access(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_full_access.txt"
    test_file.write_text("Test content")
    
    # Change permissions to full access (read/write/execute for all)
    result = change_file_permissions(str(test_file), 0o777)
    assert result is True
    
    # Check new permissions
    new_mode = test_file.stat().st_mode
    assert stat.S_IMODE(new_mode) == 0o777

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("non_existent_file.txt", 0o644)

def test_invalid_file_path():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o644)

def test_invalid_mode(tmp_path):
    test_file = tmp_path / "test_invalid_mode.txt"
    test_file.write_text("Test content")
    
    with pytest.raises(TypeError):
        change_file_permissions(str(test_file), "not an integer")