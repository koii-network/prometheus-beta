import os
import pytest
import pwd
from src.file_owner import get_file_owner

def test_get_file_owner_success(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")

    # Get current user
    current_user = pwd.getpwuid(os.getuid()).pw_name

    # Check file owner
    assert get_file_owner(str(test_file)) == current_user

def test_get_file_owner_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_owner("/path/to/nonexistent/file.txt")

def test_get_file_owner_existing_files():
    # Test with existing files in the repository
    test_files = [
        ".gitignore",
        "README.md",
        "requirements.txt"
    ]

    for file in test_files:
        result = get_file_owner(file)
        assert isinstance(result, str)
        assert len(result) > 0