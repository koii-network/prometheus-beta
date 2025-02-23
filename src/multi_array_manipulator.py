def multiArrayManipulator(arr, manipulations):
    """
    Manipulate a 2D integer array based on provided manipulations.
    
    :param arr: 2D list of integers to manipulate
    :param manipulations: Dictionary of manipulation operations
    :return: Manipulated 2D array
    """
    # Create a copy of the input array to avoid modifying the original
    result = [row.copy() for row in arr]
    
    # Perform multiply operation
    if manipulations.get('multiply'):
        multiply_value = manipulations['multiply']
        result = [[cell * multiply_value for cell in row] for row in result]
    
    # Perform add operation
    if manipulations.get('add'):
        add_value = manipulations['add']
        result = [[cell + add_value for cell in row] for row in result]
    
    # Perform transpose operation
    if manipulations.get('transpose', False):
        result = list(map(list, zip(*result)))
    
    return result