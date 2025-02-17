import logging
import os
import sys

def conditional_debug_log(message, debug_env_var='DEBUG'):
    """
    Conditionally log a debug message based on an environment variable.

    Args:
        message (str): The debug message to log
        debug_env_var (str, optional): Name of the environment variable to check. 
                                       Defaults to 'DEBUG'.

    Returns:
        bool: True if message was logged, False otherwise
    """
    # Check if the debug environment variable is set to a truthy value
    debug_value = str(os.environ.get(debug_env_var, '')).lower()
    is_debug_enabled = debug_value in ['1', 'true', 'yes']

    if is_debug_enabled:
        # Use sys.stderr to ensure consistent output
        sys.stderr.write(f'DEBUG: {message}\n')
        sys.stderr.flush()
        return True
    
    return False