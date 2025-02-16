import pytest
from src.kebab_case_converter import convert_to_kebab_case

def test_convert_to_kebab_case():
    # Test basic conversions
    assert convert_to_kebab_case("hello world") == "hello-world"
    assert convert_to_kebab_case("HelloWorld") == "hello-world"
    assert convert_to_kebab_case("hello_world") == "hello-world"
    
    # Test with special characters
    assert convert_to_kebab_case("Hello, World!") == "hello-world"
    assert convert_to_kebab_case("hello@world") == "hello-world"
    
    # Test with multiple spaces and hyphens
    assert convert_to_kebab_case("  hello   world  ") == "hello-world"
    assert convert_to_kebab_case("hello---world") == "hello-world"
    
    # Test with mixed case and special characters
    assert convert_to_kebab_case("User Profile Settings") == "user-profile-settings"
    assert convert_to_kebab_case("email_Address@Domain") == "email-address-domain"
    
    # Test edge cases
    assert convert_to_kebab_case("") == ""
    assert convert_to_kebab_case("   ") == ""
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_kebab_case(123)
    with pytest.raises(TypeError):
        convert_to_kebab_case(None)