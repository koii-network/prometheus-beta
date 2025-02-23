def tower_of_hanoi(n, source='A', auxiliary='B', destination='C'):
    """
    Recursive solution to the Tower of Hanoi puzzle.
    
    Args:
    n (int): Number of disks
    source (str): Source rod (default 'A')
    auxiliary (str): Auxiliary rod (default 'B')
    destination (str): Destination rod (default 'C')
    
    Prints the sequence of moves to solve the Tower of Hanoi puzzle.
    """
    # Base case: if only 1 disk, move directly from source to destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary rod
    # 2. Move the nth (largest) disk from source to destination 
    # 3. Move n-1 disks from auxiliary to destination
    
    # Move n-1 disks from source to auxiliary rod
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Main execution for 7 disks
if __name__ == "__main__":
    tower_of_hanoi(7)