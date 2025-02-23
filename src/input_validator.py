import logging
import re

def validate_and_log_input(input_value, validation_rules=None):
    """
    Validate input based on specified rules and log validation messages.
    
    Args:
        input_value (str): The input to validate
        validation_rules (dict, optional): Dictionary of validation rules. 
            Supported keys:
            - 'min_length': Minimum allowed length
            - 'max_length': Maximum allowed length
            - 'regex': Regex pattern to match
            - 'required': Whether input is required
    
    Returns:
        tuple: (is_valid, validation_messages)
            is_valid (bool): Whether the input passed all validations
            validation_messages (list): List of validation messages
    
    Raises:
        TypeError: If input_value is not a string
    """
    # Configure logging
    logger = logging.getLogger(__name__)
    validation_messages = []
    is_valid = True

    # Validate input type
    if not isinstance(input_value, str):
        logger.error(f"Invalid input type. Expected string, got {type(input_value)}")
        return False, ["Input must be a string"]

    # Trim whitespace
    input_value = input_value.strip()

    # Check if input is required
    if validation_rules and validation_rules.get('required', False) and not input_value:
        message = "Input is required"
        logger.warning(message)
        validation_messages.append(message)
        is_valid = False

    # Length validations
    if validation_rules:
        # Minimum length check
        if 'min_length' in validation_rules and len(input_value) < validation_rules['min_length']:
            message = f"Input must be at least {validation_rules['min_length']} characters long"
            logger.warning(message)
            validation_messages.append(message)
            is_valid = False

        # Maximum length check
        if 'max_length' in validation_rules and len(input_value) > validation_rules['max_length']:
            message = f"Input must be no more than {validation_rules['max_length']} characters long"
            logger.warning(message)
            validation_messages.append(message)
            is_valid = False

        # Regex pattern check
        if 'regex' in validation_rules:
            pattern = validation_rules['regex']
            if not re.match(pattern, input_value):
                message = "Input does not match required pattern"
                logger.warning(message)
                validation_messages.append(message)
                is_valid = False

    # Log overall validation result
    if is_valid:
        logger.info("Input validation passed")
    else:
        logger.error("Input validation failed")

    return is_valid, validation_messages