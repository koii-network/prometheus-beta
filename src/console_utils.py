import os
import platform

def clear_console_and_log(message):
    """
    Clear the console and then log a message.
    
    Args:
        message (str): The message to log after clearing the console.
    """
    # Determine the operating system and use appropriate clear command
    system = platform.system().lower()
    
    if system == 'windows':
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')
    
    # Log the message after clearing
    print(message)