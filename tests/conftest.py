import pytest
import random

def pytest_configure(config):
    """Set a fixed random seed for consistent testing"""
    random.seed(42)