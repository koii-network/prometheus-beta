import pytest
from datetime import datetime

@pytest.fixture
def mock_datetime():
    return datetime.now()