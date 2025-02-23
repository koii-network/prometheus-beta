def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all possible solutions.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of all possible solutions, where each solution is a list of 
              queen positions represented as column indices for each row.
    """
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col] without conflicts.
        
        Args:
            board (list): Current board state
            row (int): Current row to place the queen
            col (int): Current column to place the queen
        
        Returns:
            bool: True if queen can be placed safely, False otherwise
        """
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

    def solve(board, col, solutions):
        """
        Recursive backtracking function to solve N-Queens problem.
        
        Args:
            board (list): Current board state
            col (int): Current column being processed
            solutions (list): List to store valid solutions
        """
        # Base case: If all queens are placed, add solution
        if col >= n:
            solution = []
            for i in range(n):
                solution.append(board[i].index(1))
            solutions.append(solution)
            return
        
        # Consider this column and try placing queen in all rows 
        for row in range(n):
            # Check if queen can be placed on board[row][col]
            if is_safe(board, row, col):
                # Place queen
                board[row][col] = 1
                
                # Recur to place rest of the queens
                solve(board, col + 1, solutions)
                
                # Backtrack and remove queen from board[row][col]
                board[row][col] = 0

    # Initialize board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Start from the first column
    solve(board, 0, solutions)
    
    return solutions