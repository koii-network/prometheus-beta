import re
import uuid
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """Test that the generate_uuid function returns a valid UUID."""
    generated_uuid = generate_uuid()
    
    # Check that the returned value is a string
    assert isinstance(generated_uuid, str), "Generated UUID should be a string"
    
    # Validate UUID format using regex for UUID v4
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "Generated UUID does not match UUID v4 format"
    
def test_generate_uuid_uniqueness():
    """Test that multiple UUID generations produce unique values."""
    uuid_set = set(generate_uuid() for _ in range(1000))
    assert len(uuid_set) == 1000, "Generated UUIDs should be unique"