from typing import List, Dict

class BallStackSorter:
    def __init__(self, initial_stacks: Dict[str, List[str]]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        :param initial_stacks: Dictionary with stack names as keys and lists of ball colors as values
        """
        self.stacks = initial_stacks
        self.moves = []

    def is_sorted(self) -> bool:
        """
        Check if all stacks have equal number of balls and each stack has only one color.
        
        :return: True if stacks are sorted, False otherwise
        """
        # Check if all stacks have the same number of balls
        stack_lengths = [len(stack) for stack in self.stacks.values()]
        if len(set(stack_lengths)) > 1:
            return False
        
        # Check if each stack has only one color
        for stack in self.stacks.values():
            if len(set(stack)) > 1:
                return False
        
        return True

    def move_ball(self, source: str, destination: str) -> None:
        """
        Move a single ball from source stack to destination stack.
        
        :param source: Name of the source stack
        :param destination: Name of the destination stack
        """
        if not self.stacks[source]:
            raise ValueError(f"No balls in source stack {source}")
        
        ball = self.stacks[source].pop()
        self.stacks[destination].append(ball)
        self.moves.append((source, destination))

    def sort_stacks(self) -> List[tuple]:
        """
        Sort the stacks by moving balls one at a time while maintaining equal distribution.
        
        :return: List of moves made during sorting
        """
        # If already sorted, return empty moves
        if self.is_sorted():
            return self.moves
        
        # Maximum possible iterations to prevent infinite loop
        max_iterations = 1000
        iterations = 0
        
        while not self.is_sorted() and iterations < max_iterations:
            # Find stacks with different colors or unequal distribution
            colors = list(self.stacks.keys())
            
            for i in range(len(colors)):
                for j in range(i+1, len(colors)):
                    source = colors[i]
                    destination = colors[j]
                    
                    # Only move if source and destination are different colors
                    # and moving the ball helps towards sorting
                    if (self.stacks[source] and 
                        self.stacks[destination] and 
                        self.stacks[source][-1] != destination):
                        self.move_ball(source, destination)
                        break
            
            iterations += 1
        
        if iterations >= max_iterations:
            raise RuntimeError("Unable to sort stacks within maximum iterations")
        
        return self.moves