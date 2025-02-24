import logging
from typing import Union, Dict, List, Any

def log_object_details(obj: Union[Dict, List, Any], log_level: int = logging.INFO) -> None:
    """
    Log the keys and values of an object (dictionary or dictionary-like).

    Args:
        obj (Union[Dict, List, Any]): The object to log. Can be a dictionary, 
                                      list, or any other object.
        log_level (int, optional): Logging level to use. Defaults to logging.INFO.

    Raises:
        TypeError: If the input is not a dictionary-like or list-like object.
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Check input type
    if not isinstance(obj, (dict, list)):
        # For non-dict/list objects, convert to string representation
        logging.log(log_level, f"Object type: {type(obj).__name__}, String Representation: {str(obj)}")
        return
    
    # Handle dictionaries
    if isinstance(obj, dict):
        logging.log(log_level, f"Dictionary with {len(obj)} entries:")
        for key, value in obj.items():
            logging.log(log_level, f"Key: {repr(key)}, Value: {repr(value)}, Type: {type(value).__name__}")
    
    # Handle lists
    elif isinstance(obj, list):
        logging.log(log_level, f"List with {len(obj)} entries:")
        for index, item in enumerate(obj):
            logging.log(log_level, f"Index: {index}, Value: {repr(item)}, Type: {type(item).__name__}")