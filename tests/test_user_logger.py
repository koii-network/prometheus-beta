import pytest
import logging
from io import StringIO
from src.user_logger import UserLogger, UserPermissionLevel

@pytest.fixture
def log_capture():
    """Capture log output for testing"""
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)
    yield log_stream
    logging.getLogger().removeHandler(handler)

def test_guest_logger(log_capture):
    logger = UserLogger(UserPermissionLevel.GUEST)
    assert logger.log("Guest message") == True
    assert "Guest message" in log_capture.getvalue()

def test_user_logger(log_capture):
    logger = UserLogger(UserPermissionLevel.USER)
    assert logger.log("User message") == True
    assert logger.log_user("User specific message") == True
    assert logger.log_admin("Admin message") == False
    assert "User message" in log_capture.getvalue()
    assert "User specific message" in log_capture.getvalue()
    assert "Admin message" not in log_capture.getvalue()

def test_admin_logger(log_capture):
    logger = UserLogger(UserPermissionLevel.ADMIN)
    assert logger.log("Admin message") == True
    assert logger.log_user("User message") == True
    assert logger.log_admin("Admin specific message") == True
    assert "Admin message" in log_capture.getvalue()
    assert "User message" in log_capture.getvalue()
    assert "Admin specific message" in log_capture.getvalue()

def test_permission_levels():
    guest_logger = UserLogger(UserPermissionLevel.GUEST)
    user_logger = UserLogger(UserPermissionLevel.USER)
    admin_logger = UserLogger(UserPermissionLevel.ADMIN)

    assert guest_logger.user_permission_level == UserPermissionLevel.GUEST
    assert user_logger.user_permission_level == UserPermissionLevel.USER
    assert admin_logger.user_permission_level == UserPermissionLevel.ADMIN