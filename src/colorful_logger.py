from termcolor import colored

def log_colored(message, color='green'):
    """
    Log a message in a specified color.
    
    Args:
        message (str): The message to log
        color (str, optional): Color of the message. 
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'. 
            Defaults to 'green'.
    
    Raises:
        ValueError: If an unsupported color is provided
    """
    supported_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    if color not in supported_colors:
        raise ValueError(f"Unsupported color. Choose from {supported_colors}")
    
    colored_message = colored(message, color)
    print(colored_message)
    return colored_message