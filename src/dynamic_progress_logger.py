import sys
import time

def log_with_progress_bar(total_steps, message_prefix="Processing", update_interval=0.1):
    """
    Log output with a dynamically updating progress bar.
    
    Args:
        total_steps (int): Total number of steps to complete
        message_prefix (str, optional): Prefix message for the progress bar. Defaults to "Processing".
        update_interval (float, optional): Time interval between progress updates. Defaults to 0.1.
    
    Returns:
        function: A progress updater function to be called for each step
    """
    def progress_updater(current_step):
        # Calculate percentage
        percentage = min(100, max(0, (current_step / total_steps) * 100))
        
        # Create progress bar
        bar_length = 50
        filled_length = int(bar_length * current_step // total_steps)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        
        # Format output
        output = f'\r{message_prefix}: [{bar}] {percentage:.1f}% ({current_step}/{total_steps} steps)'
        
        # Print and flush to ensure immediate update
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Optional small delay to control update frequency
        time.sleep(update_interval)
        
        # Clear the line if completed
        if current_step >= total_steps:
            sys.stdout.write('\n')
    
    return progress_updater