import json
import os
import datetime
import inspect

def log_session_state(session_context=None, log_path='session_logs'):
    """
    Log the state of an interactive session.
    
    Args:
        session_context (dict, optional): A dictionary containing session-specific context.
        log_path (str, optional): Directory path to store session logs. Defaults to 'session_logs'.
    
    Returns:
        str: Path to the generated log file
    """
    # Ensure log directory exists
    os.makedirs(log_path, exist_ok=True)
    
    # Collect session state information
    session_state = {
        'timestamp': datetime.datetime.now().isoformat(),
        'caller_info': {},
        'context': session_context or {}
    }
    
    # Get caller information
    try:
        caller_frame = inspect.currentframe().f_back
        session_state['caller_info'] = {
            'filename': caller_frame.f_code.co_filename,
            'function_name': caller_frame.f_code.co_name,
            'line_number': caller_frame.f_lineno
        }
    except Exception as e:
        session_state['caller_info']['error'] = str(e)
    
    # Generate unique log filename
    log_filename = f'session_log_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    log_file_path = os.path.join(log_path, log_filename)
    
    # Write log file
    with open(log_file_path, 'w') as log_file:
        json.dump(session_state, log_file, indent=4)
    
    return log_file_path