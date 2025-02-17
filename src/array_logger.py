from typing import List, Union

def log_array_as_table(arr: List[Union[str, int, float]], headers: List[str] = None) -> str:
    """
    Convert an array to a formatted table string.
    
    Args:
        arr (List): The array to be logged
        headers (List[str], optional): Optional headers for the table. Defaults to None.
    
    Returns:
        str: A formatted table representation of the array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If headers length doesn't match array element length
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If array is empty, return empty string
    if not arr:
        return ""
    
    # Determine column width
    def get_max_width(data):
        return max(len(str(item)) for item in data)
    
    # Convert all elements to strings for consistent formatting
    str_arr = [str(item) for item in arr]
    
    # If headers are provided, validate and use them
    if headers:
        if len(headers) != len(arr):
            raise ValueError("Number of headers must match the number of array elements")
        header_width = max(get_max_width(headers), get_max_width(str_arr))
        
        # Create header row
        header_line = " | ".join(header.ljust(header_width) for header in headers)
        separator = "-" * len(header_line)
        
        # Create data row
        data_line = " | ".join(item.ljust(header_width) for item in str_arr)
        
        return f"{header_line}\n{separator}\n{data_line}"
    
    # If no headers, just create a simple table
    column_width = get_max_width(str_arr)
    return "\n".join(item.ljust(column_width) for item in str_arr)