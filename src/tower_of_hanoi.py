def solve_tower_of_hanoi(n, source_rod='A', auxiliary_rod='B', destination_rod='C'):
    """
    Solve the Tower of Hanoi puzzle recursively.
    
    Args:
        n (int): Number of disks
        source_rod (str): Name of the source rod (default 'A')
        auxiliary_rod (str): Name of the auxiliary rod (default 'B')
        destination_rod (str): Name of the destination rod (default 'C')
    
    Returns:
        list: A list of move tuples showing disk movements
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Number of disks must be a non-negative integer")
    
    # List to store moves
    moves = []
    
    def hanoi_recursive(num_disks, from_rod, aux_rod, to_rod):
        """
        Internal recursive function to solve Tower of Hanoi
        
        Args:
            num_disks (int): Number of disks to move
            from_rod (str): Source rod
            aux_rod (str): Auxiliary rod
            to_rod (str): Destination rod
        """
        if num_disks == 1:
            # Base case: move the single disk
            moves.append((from_rod, to_rod))
            return
        
        # Recursive case:
        # 1. Move n-1 disks from source to auxiliary rod
        # 2. Move the largest disk from source to destination
        # 3. Move n-1 disks from auxiliary to destination
        hanoi_recursive(num_disks - 1, from_rod, to_rod, aux_rod)
        moves.append((from_rod, to_rod))
        hanoi_recursive(num_disks - 1, aux_rod, from_rod, to_rod)
    
    # Solve the Tower of Hanoi
    hanoi_recursive(n, source_rod, auxiliary_rod, destination_rod)
    
    return moves

def print_tower_of_hanoi_moves(n, source_rod='A', auxiliary_rod='B', destination_rod='C'):
    """
    Print the moves required to solve the Tower of Hanoi puzzle.
    
    Args:
        n (int): Number of disks
        source_rod (str): Name of the source rod (default 'A')
        auxiliary_rod (str): Name of the auxiliary rod (default 'B')
        destination_rod (str): Name of the destination rod (default 'C')
    """
    moves = solve_tower_of_hanoi(n, source_rod, auxiliary_rod, destination_rod)
    for move in moves:
        print(f"Move disk from rod {move[0]} to rod {move[1]}")

# Example usage
if __name__ == "__main__":
    print_tower_of_hanoi_moves(7)