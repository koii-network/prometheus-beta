def log_array_as_table(arr, headers=None):
    """
    Convert an array to a formatted table string.
    
    Args:
        arr (list): The array to be logged
        headers (list, optional): Optional headers for the table columns
    
    Returns:
        str: A formatted table representation of the array
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If no headers are provided, use default index headers
    if headers is None:
        headers = [str(i) for i in range(len(arr[0]) if arr and isinstance(arr[0], list) else 1)]
    
    # Flatten 1D arrays
    if not arr or not isinstance(arr[0], list):
        arr = [[x] for x in arr]
    
    # Ensure headers match the number of columns
    if len(headers) != len(arr[0]):
        raise ValueError("Number of headers must match the number of columns")
    
    # Calculate column widths
    col_widths = [max(len(str(headers[i])), max(len(str(row[i])) for row in arr)) for i in range(len(headers))]
    
    # Build the table string
    table_lines = []
    
    # Header
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    table_lines.append(header_line)
    
    # Separator
    separator = "-+-".join("-" * width for width in col_widths)
    table_lines.append(separator)
    
    # Rows
    for row in arr:
        row_line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        table_lines.append(row_line)
    
    return "\n".join(table_lines)