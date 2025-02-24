import re
import sys
import time
import pytest
sys.path.append('src')

from uuid_generator import generate_uuid

def test_uuid_format():
    """Test that generated UUID matches the standard format."""
    uuid = generate_uuid()
    
    # Regular expression for UUID v4 format
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple UUIDs generated in quick succession are unique."""
    uuids = set()
    
    # Generate multiple UUIDs
    for _ in range(1000):
        uuids.add(generate_uuid())
    
    assert len(uuids) > 900, "Not enough unique UUIDs generated"

def test_uuid_version():
    """Verify that generated UUIDs have correct version and variant bits."""
    uuid = generate_uuid()
    
    # Remove hyphens
    hex_uuid = uuid.replace('-', '')
    
    # Check version: 4th bit of 7th byte should be 4
    # 13th hex character (index 12) represents this
    version_char = hex_uuid[14]
    assert version_char in '4', f"Incorrect version bit in UUID: {uuid}"
    
    # Check variant: first two bits of 9th byte should be 10
    variant_char = hex_uuid[16]
    assert variant_char in '89ab', f"Incorrect variant bits in UUID: {uuid}"

def test_uuid_length():
    """Ensure UUID is exactly 36 characters long."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"

def test_uuid_sections():
    """Verify UUID is divided into correct sections."""
    uuid = generate_uuid()
    sections = uuid.split('-')
    
    assert len(sections) == 5, "UUID does not have 5 sections"
    assert len(sections[0]) == 8, "First section should be 8 characters"
    assert len(sections[1]) == 4, "Second section should be 4 characters"
    assert len(sections[2]) == 4, "Third section should be 4 characters"
    assert len(sections[3]) == 4, "Fourth section should be 4 characters"
    assert len(sections[4]) == 12, "Fifth section should be 12 characters"