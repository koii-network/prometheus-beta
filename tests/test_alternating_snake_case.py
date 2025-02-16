import pytest
from src.alternating_snake_case import convert_to_alternating_snake_case

def test_convert_to_alternating_snake_case():
    # Test basic conversion
    assert convert_to_alternating_snake_case("hello world") == "h_e_l_l_o_w_o_r_l_d"
    
    # Test with mixed case
    assert convert_to_alternating_snake_case("HelloWorld") == "h_e_l_l_o_w_o_r_l_d"
    
    # Test with existing spaces
    assert convert_to_alternating_snake_case("Hello World") == "h_e_l_l_o_w_o_r_l_d"
    
    # Test with single character
    assert convert_to_alternating_snake_case("a") == "a"
    
    # Test with empty string
    assert convert_to_alternating_snake_case("") == ""
    
    # Test with special characters and numbers
    assert convert_to_alternating_snake_case("Hello123World!") == "h_e_l_l_o_1_2_3_w_o_r_l_d_!"

def test_convert_to_alternating_snake_case_error_handling():
    # Test with non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_snake_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_snake_case(None)