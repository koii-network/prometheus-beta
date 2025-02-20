def tower_of_hanoi(n, source_rod='A', auxiliary_rod='B', destination_rod='C'):
    """
    Solve the Tower of Hanoi puzzle recursively.
    
    Args:
    n (int): Number of disks
    source_rod (str): Name of the source rod (default 'A')
    auxiliary_rod (str): Name of the auxiliary rod (default 'B')
    destination_rod (str): Name of the destination rod (default 'C')
    
    Returns:
    list: A list of move tuples (from_rod, to_rod)
    """
    # Validate input
    if n < 1:
        return []
    
    moves = []
    
    def solve_hanoi(num_disks, source, auxiliary, destination):
        """
        Recursive helper function to solve Tower of Hanoi
        
        Args:
        num_disks (int): Number of disks to move
        source (str): Source rod
        auxiliary (str): Auxiliary rod
        destination (str): Destination rod
        """
        if num_disks == 1:
            # Base case: move single disk directly
            moves.append((source, destination))
            return
        
        # Recursive case:
        # 1. Move n-1 disks from source to auxiliary rod
        solve_hanoi(num_disks - 1, source, destination, auxiliary)
        
        # 2. Move the largest disk from source to destination
        moves.append((source, destination))
        
        # 3. Move n-1 disks from auxiliary to destination rod
        solve_hanoi(num_disks - 1, auxiliary, source, destination)
    
    # Solve for 7 disks
    solve_hanoi(n, source_rod, auxiliary_rod, destination_rod)
    
    return moves

def print_tower_of_hanoi_moves(n, source_rod='A', auxiliary_rod='B', destination_rod='C'):
    """
    Print the sequence of moves for Tower of Hanoi.
    
    Args:
    n (int): Number of disks
    source_rod (str): Name of the source rod (default 'A')
    auxiliary_rod (str): Name of the auxiliary rod (default 'B')
    destination_rod (str): Name of the destination rod (default 'C')
    """
    moves = tower_of_hanoi(n, source_rod, auxiliary_rod, destination_rod)
    for move in moves:
        print(f"Move disk from rod {move[0]} to rod {move[1]}")

# Example usage 
if __name__ == "__main__":
    print_tower_of_hanoi_moves(7)