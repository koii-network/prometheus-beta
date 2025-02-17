import uuid
import re
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """Test that generate_uuid() returns a valid UUID."""
    generated_uuid = generate_uuid()
    
    # Check that the generated UUID is a string
    assert isinstance(generated_uuid, str), "Generated UUID should be a string"
    
    # Check UUID format using regex (UUID v4 format)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "Generated UUID does not match UUID v4 format"

def test_generate_uuid_uniqueness():
    """Test that multiple calls generate different UUIDs."""
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    
    assert uuid1 != uuid2, "Generated UUIDs should be unique"