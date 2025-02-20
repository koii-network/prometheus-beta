def solve_tower_of_hanoi(n, source='A', auxiliary='B', destination='C'):
    """
    Recursive solution to the Tower of Hanoi puzzle.
    
    Args:
        n (int): Number of disks
        source (str): Name of the source rod (default 'A')
        auxiliary (str): Name of the auxiliary rod (default 'B')
        destination (str): Name of the destination rod (default 'C')
    
    Returns:
        int: Total number of moves made
    """
    if n <= 0:
        return 0
    
    # Base case: if only one disk, move directly
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    
    # Recursive solution
    # 1. Move n-1 disks from source to auxiliary rod
    # 2. Move the largest disk from source to destination
    # 3. Move n-1 disks from auxiliary to destination
    moves = 0
    
    # Step 1: Move n-1 disks from source to auxiliary
    moves += solve_tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move the largest disk
    print(f"Move disk {n} from {source} to {destination}")
    moves += 1
    
    # Step 3: Move n-1 disks from auxiliary to destination
    moves += solve_tower_of_hanoi(n-1, auxiliary, source, destination)
    
    return moves

def main():
    """
    Solve Tower of Hanoi with 7 disks and print total moves.
    """
    total_moves = solve_tower_of_hanoi(7)
    print(f"Total moves for 7 disks: {total_moves}")

if __name__ == "__main__":
    main()