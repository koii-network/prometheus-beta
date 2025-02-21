import pytest
import time
from src.process_logger import log_process_progress

def test_process_logging():
    # Mock process function to simulate work
    def mock_process(total_steps):
        logged_messages = []
        def mock_log(message):
            logged_messages.append(message)
        
        @log_process_progress(total_steps=total_steps, log_func=mock_log, update_interval=0.1)
        def work():
            for i in range(total_steps):
                time.sleep(0.05)  # Simulate work
                print(f"{i+1}/{total_steps}")
            return "Complete"
        
        result = work()
        
        # Check basic logging properties
        assert result == "Complete"
        assert len(logged_messages) > 0
        
        # Verify progress messages
        for msg in logged_messages:
            assert "Progress:" in msg
            assert "steps" in msg
            assert "Elapsed time:" in msg
        
        # Check first and last messages cover full range
        first_msg = logged_messages[0]
        last_msg = logged_messages[-1]
        
        assert "0/" not in first_msg  # First meaningful update should start > 0
        assert f"{total_steps}/{total_steps}" in last_msg
        assert "100.00%" in last_msg

def test_custom_logging():
    # Test with a custom logging function
    custom_log_messages = []
    def custom_log(message):
        custom_log_messages.append(message)
    
    @log_process_progress(total_steps=5, log_func=custom_log)
    def sample_task():
        for i in range(5):
            time.sleep(0.1)
            print(f"{i+1}/5")
        return "Done"
    
    result = sample_task()
    
    assert result == "Done"
    assert len(custom_log_messages) > 0

def test_error_handling():
    # Test function that might raise an exception
    with pytest.raises(ValueError):
        @log_process_progress(total_steps=3)
        def failing_task():
            for i in range(3):
                time.sleep(0.1)
                if i == 2:
                    raise ValueError("Simulated failure")
                print(f"{i+1}/3")
        
        failing_task()