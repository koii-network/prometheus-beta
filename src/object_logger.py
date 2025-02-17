import logging

def log_object_details(obj):
    """
    Log the keys and values of a given object.
    
    Args:
        obj (dict or object): The object to log. If it's not a dictionary, 
                               it will be converted to a dictionary using vars() or __dict__.
    
    Raises:
        TypeError: If the object cannot be converted to a dictionary.
    """
    # Determine how to convert the object to a dictionary
    try:
        if isinstance(obj, dict):
            obj_dict = obj
        elif hasattr(obj, '__dict__'):
            obj_dict = vars(obj)
        elif hasattr(obj, 'to_dict'):
            obj_dict = obj.to_dict()
        else:
            raise TypeError("Object cannot be converted to a dictionary")
        
        # Configure logging if not already configured
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        
        # Log object details
        logging.info("Object Details:")
        for key, value in obj_dict.items():
            logging.info(f"{key}: {value}")
        
        return obj_dict
    except Exception as e:
        logging.error(f"Error logging object details: {e}")
        raise