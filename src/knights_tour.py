class KnightsTourSolver:
    def __init__(self, board_size=8):
        """
        Initialize the Knights Tour solver for a given board size.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

    def is_valid_move(self, board, x, y):
        """
        Check if the move is valid on the board.
        
        :param board: Current board state
        :param x: x-coordinate
        :param y: y-coordinate
        :return: True if move is valid, False otherwise
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)

    def solve_knights_tour(self, start_x, start_y):
        """
        Solve the Knight's Tour problem starting from a given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: List of (x, y) tuples representing the knight's tour, or None if no solution
        """
        # Initialize the board with -1 (unvisited)
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        # Track the tour path
        tour = []
        
        def backtrack(x, y, move_count):
            # Mark current square as visited
            board[x][y] = move_count
            tour.append((x, y))
            
            # If we've visited all squares, we've found a solution
            if move_count == self.board_size * self.board_size - 1:
                return True
            
            # Try all possible knight moves
            for dx, dy in self.moves:
                next_x, next_y = x + dx, y + dy
                
                # If move is valid and square is unvisited
                if self.is_valid_move(board, next_x, next_y):
                    # Recursively try this move
                    if backtrack(next_x, next_y, move_count + 1):
                        return True
            
            # Backtrack: undo the move if it doesn't lead to a solution
            board[x][y] = -1
            tour.pop()
            return False
        
        # Start the tour from the given position
        if backtrack(start_x, start_y, 0):
            return tour
        
        return None  # No solution found