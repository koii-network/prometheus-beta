def log_array_table(arr, headers=None):
    """
    Log an array in a formatted table format.
    
    Args:
        arr (list): The array to be logged
        headers (list, optional): Optional headers for the table columns. 
                                  If not provided, uses index numbers.
    
    Returns:
        str: Formatted table string
    
    Raises:
        TypeError: If input is not a list
        ValueError: If headers length doesn't match array element length
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If array is empty, return empty string
    if not arr:
        return ""
    
    # Determine if we're dealing with simple values or complex objects
    first_item = arr[0]
    
    # If first item is a simple type (int, str, float), treat as 1D array
    if isinstance(first_item, (int, str, float, bool)):
        # If no headers provided, use index
        if headers is None:
            headers = ['Index', 'Value']
            arr = list(enumerate(arr))
        elif len(headers) != 2:
            raise ValueError("For 1D arrays, headers must be a list of 2 elements")
    
    # If first item is a list or tuple (2D array)
    elif isinstance(first_item, (list, tuple)):
        # Validate consistency of sublists
        if not all(len(item) == len(first_item) for item in arr):
            raise ValueError("All sublists must have the same length")
        
        # If no headers provided, use column indices
        if headers is None:
            headers = [f'Column {i+1}' for i in range(len(first_item))]
        elif len(headers) != len(first_item):
            raise ValueError(f"Headers must match the number of columns ({len(first_item)})")
    
    else:
        raise TypeError("Unsupported array type. Must be list of simple types or list of lists/tuples")
    
    # Prepare the table
    # Calculate column widths
    col_widths = [max(len(str(headers[j])), max(len(str(row[j])) for row in arr)) for j in range(len(headers))]
    
    # Create format string
    format_string = ' | '.join(f'{{:{width}}}' for width in col_widths)
    
    # Build table
    table_lines = []
    
    # Add header
    table_lines.append(format_string.format(*headers))
    
    # Add separator
    table_lines.append('-' * (sum(col_widths) + 3 * (len(headers) - 1)))
    
    # Add rows
    for row in arr:
        table_lines.append(format_string.format(*row))
    
    return '\n'.join(table_lines)