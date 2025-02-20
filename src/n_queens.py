def solve_n_queens(n):
    """
    Solve the N-Queens problem for a given board size.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of solutions, where each solution is a list of queen positions.
               Each position is represented as a column index for each row.
    """
    def is_safe(board, row, col):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve_queens_util(board, col, solutions):
        # Base case: If all queens are placed, add the solution
        if col >= n:
            # Convert board to solution format (column index for each row)
            solution = []
            for row in range(n):
                solution.append(board[row].index(1))
            solutions.append(solution)
            return True
        
        # Consider this column and try placing queens in all rows one by one
        for row in range(n):
            # Check if queen can be placed on board[row][col]
            if is_safe(board, row, col):
                # Place the queen
                board[row][col] = 1
                
                # Recur to place rest of the queens
                solve_queens_util(board, col + 1, solutions)
                
                # If placing queen doesn't lead to a solution, 
                # then remove queen from board
                board[row][col] = 0
        
        return False

    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Start from the first column
    solve_queens_util(board, 0, solutions)
    
    return solutions