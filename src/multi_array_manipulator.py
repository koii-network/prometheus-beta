def multiArrayManipulator(arr, manipulations):
    """
    Perform various manipulations on a 2D integer array.
    
    :param arr: A 2D list of integers
    :param manipulations: A dictionary with manipulation instructions
    :return: Manipulated 2D list
    """
    # Create a deep copy to avoid modifying the original array
    result = [row.copy() for row in arr]
    
    # Handle multiply operation
    if manipulations.get('multiply'):
        factor = manipulations['multiply']
        result = [[val * factor for val in row] for row in result]
    
    # Handle add operation
    if manipulations.get('add'):
        addend = manipulations['add']
        result = [[val + addend for val in row] for row in result]
    
    # Handle transpose operation
    if manipulations.get('transpose', False):
        result = list(map(list, zip(*result)))
    
    return result