import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_archiver import create_tar_archive

def test_create_tar_archive():
    # Create a temporary directory with some test files
    with tempfile.TemporaryDirectory() as source_dir:
        # Create some test files
        with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(source_dir, 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        
        # Create a temporary location for the archive
        with tempfile.TemporaryDirectory() as temp_dir:
            archive_path = os.path.join(temp_dir, 'test_archive.tar.gz')
            
            # Create tar archive
            result_path = create_tar_archive(source_dir, archive_path)
            
            # Verify archive was created
            assert os.path.exists(result_path)
            assert result_path == archive_path
            
            # Verify archive contents
            with tarfile.open(result_path, 'r:gz') as tar:
                extracted_names = tar.getnames()
                assert len(extracted_names) > 0
                assert 'file1.txt' in extracted_names
                assert 'file2.txt' in extracted_names

def test_invalid_source_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, 'non_existent')
        archive_path = os.path.join(temp_dir, 'test_archive.tar.gz')
        
        with pytest.raises(ValueError, match="Source directory does not exist"):
            create_tar_archive(non_existent_dir, archive_path)

def test_different_compression_types():
    compression_types = ['gz', 'bz2', 'xz', None]
    
    with tempfile.TemporaryDirectory() as source_dir:
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('Test content')
        
        with tempfile.TemporaryDirectory() as temp_dir:
            for compress_type in compression_types:
                archive_ext = {
                    'gz': '.tar.gz',
                    'bz2': '.tar.bz2',
                    'xz': '.tar.xz',
                    None: '.tar'
                }
                
                archive_path = os.path.join(temp_dir, f'archive{archive_ext[compress_type]}')
                create_tar_archive(source_dir, archive_path, compress_type)
                
                assert os.path.exists(archive_path)

def test_invalid_compression_type():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as temp_dir:
            archive_path = os.path.join(temp_dir, 'test_archive.tar')
            
            with pytest.raises(ValueError, match="Unsupported compression type"):
                create_tar_archive(source_dir, archive_path, 'invalid_type')