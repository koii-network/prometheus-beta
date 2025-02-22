# File Utilities

## Function: remove_empty_lines

A utility function to remove empty lines from a file.

### Usage
```python
from src.remove_empty_lines import remove_empty_lines

# Remove empty lines from the same file
remove_empty_lines('input.txt')

# Remove empty lines to a new output file
remove_empty_lines('input.txt', 'output.txt')
```

### Features
- Removes lines that are completely empty or contain only whitespace
- Option to overwrite original file or write to a new file
- Returns the number of empty lines removed
- Handles various edge cases like empty files

### Error Handling
- Raises `FileNotFoundError` if input file does not exist
- Raises `PermissionError` for file access issues