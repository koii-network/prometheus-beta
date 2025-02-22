import os
import pytest
from src.sum_pairs_with_difference import sum_pairs_with_difference_nine

def test_basic_functionality(tmp_path):
    # Create a test file with numbers
    test_file = tmp_path / "numbers.txt"
    test_file.write_text("10\n1\n19\n5\n14\n")
    
    # 10 and 1 have a difference of 9, so their sum is 11
    # 19 and 10 have a difference of 9, so their sum is 29
    assert sum_pairs_with_difference_nine(str(test_file)) == 40

def test_no_pairs_with_difference_nine(tmp_path):
    # Create a test file with no pairs having difference of 9
    test_file = tmp_path / "numbers.txt"
    test_file.write_text("1\n2\n3\n4\n5\n")
    
    assert sum_pairs_with_difference_nine(str(test_file)) == 0

def test_multiple_pairs_with_difference_nine(tmp_path):
    # Create a test file with multiple pairs
    test_file = tmp_path / "numbers.txt"
    test_file.write_text("1\n10\n19\n28\n37\n")
    
    # Pairs: (1,10), (10,19), (19,28), (28,37)
    assert sum_pairs_with_difference_nine(str(test_file)) == 222

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_difference_nine("non_existent_file.txt")

def test_invalid_content(tmp_path):
    # Create a file with non-numeric content
    test_file = tmp_path / "invalid.txt"
    test_file.write_text("1\n2\nabc\n4\n")
    
    with pytest.raises(ValueError):
        sum_pairs_with_difference_nine(str(test_file))

def test_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    assert sum_pairs_with_difference_nine(str(test_file)) == 0