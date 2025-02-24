def solve_n_queens(n):
    """
    Solve the N-Queens problem for an NxN chessboard.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of all possible queen arrangements, where each arrangement 
              is represented by a list of column positions for each row.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Validate input
    if n < 1:
        raise ValueError("Board size must be at least 1")
    
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col].
        
        Args:
            board (list): Current board state
            row (int): Current row to place the queen
            col (int): Current column to place the queen
        
        Returns:
            bool: True if queen can be placed safely, False otherwise
        """
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve(board, col, solutions):
        """
        Recursive backtracking function to solve N-Queens problem.
        
        Args:
            board (list): Current board state
            col (int): Current column being processed
            solutions (list): List to store valid solutions
        
        Returns:
            None
        """
        # Base case: If all queens are placed, add solution
        if col >= n:
            # Extract column positions for each row
            solution = []
            for row in board:
                solution.append(row.index(1))
            solutions.append(solution)
            return
        
        # Consider this column and try placing queen in all rows
        for row in range(n):
            # Create a copy of the current board state
            board_copy = [row[:] for row in board]
            
            # If queen can be placed safely
            if is_safe(board_copy, row, col):
                # Place queen
                board_copy[row][col] = 1
                
                # Recur to place rest of the queens
                solve(board_copy, col + 1, solutions)
                # Note: We don't need to backtrack as we create a new board each time
    
    # Initialize empty board
    initial_board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Start solving from first column
    solve(initial_board, 0, solutions)
    
    return solutions