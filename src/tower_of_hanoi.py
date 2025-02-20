def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Recursive implementation of Tower of Hanoi puzzle.
    
    Args:
        n (int): Number of disks
        source (str): Name of the source rod
        auxiliary (str): Name of the auxiliary rod
        destination (str): Name of the destination rod
    
    Prints the sequence of moves to solve the Tower of Hanoi puzzle.
    
    Raises:
        ValueError: If source, auxiliary, and destination rods are not unique
    """
    if source == auxiliary or source == destination or auxiliary == destination:
        raise ValueError("Source, auxiliary, and destination rods must be unique")
    
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 disks from source to auxiliary rod
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination rod
    tower_of_hanoi(n-1, auxiliary, source, destination)

def solve_tower_of_hanoi():
    """
    Solve Tower of Hanoi puzzle with 7 disks.
    """
    num_disks = 7
    tower_of_hanoi(num_disks, 'A', 'B', 'C')