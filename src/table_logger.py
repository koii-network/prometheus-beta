def log_array_as_table(arr, headers=None):
    """
    Log an array in a formatted table format.
    
    Args:
        arr (list): The array to be logged
        headers (list, optional): Optional headers for the table. 
                                  If not provided, uses default numeric indexing.
    
    Returns:
        str: Formatted table string
    
    Raises:
        TypeError: If input is not a list
        ValueError: If headers length doesn't match array element length
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty array
    if not arr:
        return "Empty table"
    
    # Determine if array contains nested data
    if not all(isinstance(item, (list, tuple)) for item in arr):
        # If array contains simple types, convert to list of lists
        arr = [[item] for item in arr]
    
    # Handle headers
    if headers is None:
        # Use numeric column headers if not provided
        headers = [str(i) for i in range(len(arr[0]))]
    elif len(headers) != len(arr[0]):
        raise ValueError("Headers must match the number of columns in the array")
    
    # Calculate column widths
    col_widths = [max(len(str(headers[j])), 
                      max(len(str(row[j])) for row in arr)) 
                  for j in range(len(headers))]
    
    # Build table string
    table_lines = []
    
    # Header row
    header_line = " | ".join(f"{headers[j]:<{col_widths[j]}}" for j in range(len(headers)))
    table_lines.append(header_line)
    
    # Separator line
    separator_line = "-+-".join("-" * width for width in col_widths)
    table_lines.append(separator_line)
    
    # Data rows
    for row in arr:
        data_line = " | ".join(f"{str(row[j]):<{col_widths[j]}}" for j in range(len(row)))
        table_lines.append(data_line)
    
    return "\n".join(table_lines)