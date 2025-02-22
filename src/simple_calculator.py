def simple_calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operator (str): Arithmetic operator (+, -, *, /)
    
    Returns:
        float: Result of the arithmetic operation
    
    Raises:
        ValueError: If an invalid operator is provided
        ZeroDivisionError: If division by zero is attempted
    """
    # Convert inputs to float to handle both int and float
    num1, num2 = float(num1), float(num2)
    
    # Perform calculation based on operator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError(f"Invalid operator: {operator}. Supported operators are +, -, *, /")