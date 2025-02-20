def multiArrayManipulator(arr, manipulations):
    """
    Manipulate a 2D integer array based on provided manipulations.
    
    Operations applied in order: multiply, add, transpose
    
    :param arr: 2D list of integers
    :param manipulations: Dictionary of manipulation operations
    :return: Manipulated 2D list of integers
    """
    # Create a copy to avoid modifying the original array
    result = [row.copy() for row in arr]
    
    # Perform multiply operation
    if 'multiply' in manipulations:
        multiplier = manipulations['multiply']
        result = [[val * multiplier for val in row] for row in result]
    
    # Perform add operation
    if 'add' in manipulations:
        addend = manipulations['add']
        result = [[val + addend for val in row] for row in result]
    
    # Perform transpose operation
    if 'transpose' in manipulations and manipulations['transpose']:
        result = list(map(list, zip(*result)))
    
    return result