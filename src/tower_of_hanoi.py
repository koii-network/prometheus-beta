def tower_of_hanoi(n, source_rod='A', target_rod='C', auxiliary_rod='B'):
    """
    Recursive solution to Tower of Hanoi puzzle.
    
    Args:
        n (int): Number of disks
        source_rod (str): Name of the source rod (default 'A')
        target_rod (str): Name of the target rod (default 'C')
        auxiliary_rod (str): Name of the auxiliary rod (default 'B')
    
    Returns:
        list: List of moves performed
    """
    # Validate input
    if n < 1:
        return []
    
    moves = []
    
    def _solve_hanoi(num_disks, source, target, auxiliary):
        """Internal recursive helper function to solve Tower of Hanoi"""
        if num_disks == 1:
            # Base case: move one disk directly
            move = f"Move disk 1 from {source} to {target}"
            moves.append(move)
            print(move)
            return
        
        # Recursive case
        # 1. Move n-1 disks from source to auxiliary
        _solve_hanoi(num_disks - 1, source, auxiliary, target)
        
        # 2. Move the nth disk from source to target
        move = f"Move disk {num_disks} from {source} to {target}"
        moves.append(move)
        print(move)
        
        # 3. Move n-1 disks from auxiliary to target
        _solve_hanoi(num_disks - 1, auxiliary, target, source)
    
    # Start solving with 7 disks
    _solve_hanoi(n, source_rod, target_rod, auxiliary_rod)
    
    return moves

# Demonstrate with 7 disks when script is run directly
if __name__ == "__main__":
    tower_of_hanoi(7)