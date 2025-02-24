def solve_n_queens(n):
    """
    Solve the N-Queens problem for a given board size.
    
    Args:
        n (int): Size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of solutions, where each solution is a list of queen positions.
              Each position is represented as a column index for each row.
    
    Raises:
        ValueError: If n is less than 1 or input is not a positive integer.
    """
    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("Board size must be a positive integer")
    
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col] safely.
        
        Args:
            board (list): Current board state represented by queen column positions.
            row (int): Current row being checked.
            col (int): Current column being checked.
        
        Returns:
            bool: True if queen can be placed safely, False otherwise.
        """
        # Check this row on left side
        for i in range(row):
            # Check column
            if board[i] == col:
                return False
            
            # Check diagonals
            if (board[i] - col == i - row) or (col - board[i] == i - row):
                return False
        
        return True
    
    def backtrack(board, row):
        """
        Backtracking function to solve N-Queens problem.
        
        Args:
            board (list): Current board state.
            row (int): Current row being processed.
        
        Returns:
            list: List of valid solutions.
        """
        # Base case: all queens are placed
        if row == n:
            return [board.copy()]
        
        solutions = []
        
        # Try placing queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                
                # Recursively place queens in subsequent rows
                solutions.extend(backtrack(board, row + 1))
        
        return solutions
    
    # Initialize an empty board
    board = [-1] * n
    
    # Solve and return solutions
    return backtrack(board, 0)

def count_n_queens_solutions(n):
    """
    Count the number of distinct solutions to the N-Queens problem.
    
    Args:
        n (int): Size of the chessboard and number of queens to place.
    
    Returns:
        int: Number of distinct solutions.
    
    Raises:
        ValueError: If n is less than 1 or input is not a positive integer.
    """
    return len(solve_n_queens(n))