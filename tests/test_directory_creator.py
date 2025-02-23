import os
import pytest
import shutil
import tempfile

from src.directory_creator import create_directory

class TestDirectoryCreator:
    def setup_method(self):
        # Create a temporary base directory for testing
        self.test_base_dir = tempfile.mkdtemp()

    def teardown_method(self):
        # Remove the temporary base directory and its contents
        shutil.rmtree(self.test_base_dir)

    def test_create_simple_directory(self):
        # Test creating a simple directory
        test_dir = os.path.join(self.test_base_dir, 'new_dir')
        result = create_directory(test_dir)
        
        assert result is True
        assert os.path.isdir(test_dir)
        assert os.access(test_dir, os.R_OK | os.W_OK | os.X_OK)

    def test_create_existing_directory(self):
        # Test attempting to create an already existing directory
        test_dir = os.path.join(self.test_base_dir, 'existing_dir')
        os.mkdir(test_dir)
        
        result = create_directory(test_dir)
        assert result is False

    def test_create_directory_with_parents_flag(self):
        # Test creating nested directories with parents flag
        test_dir = os.path.join(self.test_base_dir, 'parent', 'child', 'grandchild')
        result = create_directory(test_dir, parents=True)
        
        assert result is True
        assert os.path.isdir(test_dir)

    def test_create_directory_without_parents_flag(self):
        # Test creating nested directories without parents flag should fail
        test_dir = os.path.join(self.test_base_dir, 'parent', 'child')
        
        with pytest.raises(OSError):
            create_directory(test_dir)

    def test_create_directory_invalid_path(self):
        # Test creating a directory with an invalid path
        with pytest.raises(ValueError):
            create_directory('')

    def test_create_directory_custom_mode(self):
        # Test creating a directory with a custom mode
        test_dir = os.path.join(self.test_base_dir, 'custom_mode_dir')
        result = create_directory(test_dir, mode=0o700)
        
        assert result is True
        # Check if the directory has the specified permissions
        assert oct(os.stat(test_dir).st_mode)[-3:] == '700'