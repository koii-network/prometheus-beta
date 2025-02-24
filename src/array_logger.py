from typing import List, Union, Any

def log_array_table(arr: List[Union[Any, List[Any]]], 
                    headers: List[str] = None, 
                    indent: int = 0) -> str:
    """
    Log an array in a formatted table, supporting nested arrays and various data types.
    
    Args:
        arr (List): The array to be logged
        headers (List[str], optional): Custom headers for the table. Defaults to None.
        indent (int, optional): Number of spaces to indent the table. Defaults to 0.
    
    Returns:
        str: Formatted table representation of the array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If headers length does not match row length
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If array is empty, return empty string
    if not arr:
        return ""
    
    # Determine if the array contains nested arrays
    is_nested = any(isinstance(item, list) for item in arr)
    
    # If not nested, convert to list of lists for consistent processing
    if not is_nested:
        arr = [[item] for item in arr]
    
    # Auto-generate headers if not provided
    if headers is None:
        max_depth = max(len(row) if isinstance(row, list) else 1 for row in arr)
        headers = [f"Column {i+1}" for i in range(max_depth)]
    
    # Validate headers match row length
    if any(len(row) != len(headers) for row in arr if isinstance(row, list)):
        raise ValueError("Headers must match the number of columns in the array")
    
    # Calculate column widths
    col_widths = []
    for i in range(len(headers)):
        # Find max width comparing header and all column values
        col_values = [row[i] if i < len(row) else '' for row in arr]
        col_values.append(headers[i])
        col_widths.append(max(len(str(val)) for val in col_values))
    
    # Build table
    lines = []
    
    # Indent spaces
    indent_str = ' ' * indent
    
    # Header
    header_line = indent_str + ' | '.join(
        headers[i].ljust(col_widths[i]) for i in range(len(headers))
    )
    lines.append(header_line)
    
    # Separator
    separator = indent_str + '-+-'.join(
        '-' * col_widths[i] for i in range(len(headers))
    )
    lines.append(separator)
    
    # Rows
    for row in arr:
        # Handle both nested and non-nested rows
        if not isinstance(row, list):
            row = [row]
        
        # Pad row if shorter than headers
        row_str = indent_str + ' | '.join(
            str(row[i] if i < len(row) else '').ljust(col_widths[i]) 
            for i in range(len(headers))
        )
        lines.append(row_str)
    
    return '\n'.join(lines)