import pytest
from src.csv_sum_parser import parse_csv_sum

def test_parse_csv_sum_basic():
    assert parse_csv_sum("1,2,3,4") == 10

def test_parse_csv_sum_with_spaces():
    assert parse_csv_sum(" 1 , 2 , 3 , 4 ") == 10

def test_parse_csv_sum_single_number():
    assert parse_csv_sum("42") == 42

def test_parse_csv_sum_empty_string():
    assert parse_csv_sum("") == 0

def test_parse_csv_sum_negative_numbers():
    assert parse_csv_sum("-1,2,-3,4") == 2

def test_parse_csv_sum_invalid_input():
    with pytest.raises(ValueError, match="Input string must contain only integers separated by commas"):
        parse_csv_sum("1,2,a,4")

def test_parse_csv_sum_non_numeric():
    with pytest.raises(ValueError, match="Input string must contain only integers separated by commas"):
        parse_csv_sum("1,2.5,3,4")