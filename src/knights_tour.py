class KnightsTourSolver:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

    def is_valid_move(self, x, y, board):
        """Check if the move is within the board and not visited."""
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)

    def solve_knights_tour(self, start_x, start_y):
        """
        Solve the Knight's Tour problem starting from a given position.
        
        Args:
            start_x (int): Starting x-coordinate (row)
            start_y (int): Starting y-coordinate (column)
        
        Returns:
            list: A list of (x, y) tuples representing the knight's path,
                  or None if no solution is found
        """
        # Initialize board with -1 (unvisited)
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        path = []

        def backtrack(x, y, move_count):
            # Mark the current square as visited
            board[x][y] = move_count
            path.append((x, y))

            # If we've visited all squares, we've found a solution
            if move_count == self.board_size * self.board_size - 1:
                return True

            # Try all possible knight moves
            for dx, dy in self.moves:
                next_x, next_y = x + dx, y + dy
                
                # If the next move is valid and unvisited
                if self.is_valid_move(next_x, next_y, board):
                    # Recursively try this move
                    if backtrack(next_x, next_y, move_count + 1):
                        return True

            # If no solution found, backtrack
            board[x][y] = -1
            path.pop()
            return False

        # Start the tour from the given starting position
        if backtrack(start_x, start_y, 0):
            return path
        
        return None  # No solution found