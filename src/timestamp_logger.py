import datetime
import os
import json
from typing import Any, Union

def log_data(data: Any, log_file: str = 'logs/data_log.json') -> None:
    """
    Log data with a timestamp to a JSON log file.

    Args:
        data (Any): The data to be logged. Can be of any JSON-serializable type.
        log_file (str, optional): Path to the log file. Defaults to 'logs/data_log.json'.

    Raises:
        TypeError: If data cannot be JSON serialized.
        IOError: If there are issues creating the log directory or writing to the file.
    """
    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Create log entry with timestamp
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'data': data
    }

    # Append to log file
    try:
        # If file exists, read and append
        if os.path.exists(log_file):
            with open(log_file, 'r+') as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
                
                logs.append(log_entry)
                f.seek(0)
                json.dump(logs, f, indent=2)
                f.truncate()
        else:
            # Create new log file
            with open(log_file, 'w') as f:
                json.dump([log_entry], f, indent=2)
    except (TypeError, OverflowError) as e:
        raise TypeError(f"Unable to serialize data: {e}")
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")