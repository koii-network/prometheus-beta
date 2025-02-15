import os
import pytest
import shutil
import tempfile

from src.directory_deletion import delete_directory

def test_delete_directory_success():
    # Create a temporary directory with some files
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some nested files and directories
        os.makedirs(os.path.join(temp_dir, 'nested', 'sub_nested'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(temp_dir, 'nested', 'file2.txt'), 'w') as f:
            f.write('test')
        
        # Attempt to delete directory
        delete_directory(temp_dir)
        
        # Assert directory is deleted
        assert not os.path.exists(temp_dir)
    except Exception as e:
        # Cleanup in case of test failure
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        raise e

def test_delete_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        delete_directory('/path/to/nonexistent/directory')

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            with pytest.raises(NotADirectoryError):
                delete_directory(temp_file.name)
        finally:
            # Cleanup
            os.unlink(temp_file.name)

def test_delete_invalid_input_type():
    with pytest.raises(TypeError):
        delete_directory(123)
    with pytest.raises(TypeError):
        delete_directory(None)