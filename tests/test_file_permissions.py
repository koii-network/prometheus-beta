import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file with specific permissions
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    test_file.chmod(0o755)  # rwxr-xr-x

    # Get permissions
    permissions = get_file_permissions(str(test_file))

    # Validate numeric permissions
    assert permissions['numeric'] == '0o755'
    
    # Validate readable permissions
    assert permissions['readable'] == 'rwxr-xr-x'
    
    # Validate individual permissions
    assert permissions['owner_read'] == True
    assert permissions['owner_write'] == True
    assert permissions['owner_execute'] == True
    assert permissions['group_read'] == True
    assert permissions['group_execute'] == True
    assert permissions['group_write'] == False
    assert permissions['others_read'] == True
    assert permissions['others_execute'] == True
    assert permissions['others_write'] == False

def test_get_file_permissions_nonexistent_file():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        get_file_permissions('/path/to/nonexistent/file.txt')

def test_get_file_permissions_invalid_input():
    # Test for TypeError with non-string input
    with pytest.raises(TypeError):
        get_file_permissions(123)

def test_get_file_permissions_different_modes(tmp_path):
    # Test multiple different permission modes
    test_cases = [
        (0o644, 'rw-r--r--'),  # standard read-write for owner, read-only for others
        (0o600, 'rw-------'),  # owner-only read-write
        (0o755, 'rwxr-xr-x'),  # standard executable
        (0o700, 'rwx------')   # owner-only everything
    ]

    for mode, expected_readable in test_cases:
        test_file = tmp_path / f"test_mode_{mode}.txt"
        test_file.write_text("Test content")
        test_file.chmod(mode)

        permissions = get_file_permissions(str(test_file))
        assert permissions['numeric'] == oct(mode)
        assert permissions['readable'] == expected_readable