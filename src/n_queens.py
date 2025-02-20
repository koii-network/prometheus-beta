def solve_n_queens(n):
    """
    Solve the N-Queens problem for an NxN chessboard.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of solutions, where each solution is a list of queen positions.
               Each position is represented as a list [row, col].
    """
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col] safely.
        
        Args:
            board (list): Current state of queens on the board
            row (int): Row to check
            col (int): Column to check
        
        Returns:
            bool: True if the position is safe, False otherwise
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
    
    def solve(board, col, queens_positions):
        """
        Recursive backtracking function to solve N-Queens.
        
        Args:
            board (list): Current state of the chessboard
            col (int): Current column being processed
            queens_positions (list): List of queen positions
        
        Returns:
            list: Solutions found
        """
        # Base case: if all queens are placed, return the solution
        if col >= n:
            return [queens_positions.copy()]
        
        solutions = []
        
        # Consider this column and try placing queens in all rows one by one
        for row in range(n):
            # Check if queen can be placed on board[row][col]
            if is_safe(board, row, col):
                # Place the queen
                board[row][col] = 1
                queens_positions.append([row, col])
                
                # Recur to place rest of the queens
                solutions.extend(solve(board, col + 1, queens_positions))
                
                # Backtrack: remove queen from board[row][col]
                board[row][col] = 0
                queens_positions.pop()
        
        return solutions
    
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Find all solutions
    return solve(board, 0, [])