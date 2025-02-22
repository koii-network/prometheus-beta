def solve_knights_tour(start_x, start_y):
    """
    Solve the Knight's Tour problem on an 8x8 chessboard.
    
    Args:
        start_x (int): Starting x-coordinate (0-7)
        start_y (int): Starting y-coordinate (0-7)
    
    Returns:
        list: A list of tuples representing the sequence of moves, 
              or None if no tour is possible
    """
    # Possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # 8x8 chessboard
    board_size = 8
    
    # Initialize the board with -1 (unvisited)
    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    tour = []
    
    def is_valid_move(x, y):
        """Check if the move is within the board and not visited"""
        return (0 <= x < board_size and 
                0 <= y < board_size and 
                board[x][y] == -1)
    
    def backtrack(x, y, move_count):
        """Recursive backtracking to find the Knight's Tour"""
        # Mark current square as visited
        board[x][y] = move_count
        tour.append((x, y))
        
        # If we've visited all squares, we found a tour
        if move_count == board_size * board_size - 1:
            return True
        
        # Try all possible knight moves
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            
            # If the next move is valid, recursively try it
            if is_valid_move(next_x, next_y):
                if backtrack(next_x, next_y, move_count + 1):
                    return True
        
        # If no solution found, backtrack
        board[x][y] = -1
        tour.pop()
        return False
    
    # Start the tour from the given starting position
    if backtrack(start_x, start_y, 0):
        return tour
    
    return None  # No tour found