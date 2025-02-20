import os
import pytest
from src.pair_sum_with_diff_9 import sum_pairs_with_diff_9

def test_simple_case(tmp_path):
    # Create a test file with simple pairs
    test_file = tmp_path / "numbers.txt"
    test_file.write_text("5\n14\n10\n1\n")
    
    # 5 and 14 form a pair (diff of 9), same for 10 and 1
    assert sum_pairs_with_diff_9(str(test_file)) == 30

def test_multiple_pairs(tmp_path):
    # Test multiple pairs in a single file
    test_file = tmp_path / "multiple_pairs.txt"
    test_file.write_text("5\n14\n10\n1\n23\n32\n")
    
    # (5,14), (10,1), (23,32) are pairs
    assert sum_pairs_with_diff_9(str(test_file)) == 85

def test_no_pairs(tmp_path):
    # Test file with no pairs
    test_file = tmp_path / "no_pairs.txt"
    test_file.write_text("1\n2\n3\n4\n")
    
    assert sum_pairs_with_diff_9(str(test_file)) == 0

def test_empty_file(tmp_path):
    # Test empty file
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    assert sum_pairs_with_diff_9(str(test_file)) == 0

def test_file_not_found():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_diff_9("non_existent_file.txt")

def test_non_numeric_content(tmp_path):
    # Test file with non-numeric content
    test_file = tmp_path / "invalid.txt"
    test_file.write_text("5\nabc\n14\n")
    
    with pytest.raises(ValueError):
        sum_pairs_with_diff_9(str(test_file))