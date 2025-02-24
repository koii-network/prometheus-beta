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
    
    # Prepare rows: convert non-list items to single-item lists
    processed_rows = []
    for item in arr:
        if isinstance(item, list):
            processed_rows.append(item)
        else:
            processed_rows.append([item])
    
    # Determine max column count
    max_cols = max(len(row) for row in processed_rows)
    
    # Auto-generate headers if not provided
    if headers is None:
        headers = [f"Column {i+1}" for i in range(max_cols)]
    
    # Validate headers match row length
    if len(headers) != max_cols:
        raise ValueError("Headers must match the number of columns in the array")
    
    # Calculate column widths
    col_widths = []
    for i in range(max_cols):
        # Collect values for this column, padding with empty string if needed
        col_values = [str(row[i] if i < len(row) else '') for row in processed_rows]
        col_values.append(headers[i])
        col_widths.append(max(len(val) for val in col_values))
    
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
    for row in processed_rows:
        # Pad row if shorter than headers
        row_str = indent_str + ' | '.join(
            str(row[i] if i < len(row) else '').ljust(col_widths[i]) 
            for i in range(len(headers))
        )
        lines.append(row_str)
    
    return '\n'.join(lines)