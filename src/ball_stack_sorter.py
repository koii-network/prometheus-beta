from typing import List, Dict

class BallStackSorter:
    def __init__(self, stacks: Dict[str, List[str]]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        Args:
            stacks (Dict[str, List[str]]): A dictionary with stack names as keys 
                                           and lists of colored balls as values.
        """
        self.stacks = stacks
        self.total_balls = sum(len(stack) for stack in stacks.values())
        self.target_stack_size = self.total_balls // len(stacks)
        
        # Validate initial state
        if self.total_balls % len(stacks) != 0:
            raise ValueError("Total number of balls must be divisible equally among stacks")
    
    def can_move(self, from_stack: str, to_stack: str) -> bool:
        """
        Check if a ball can be moved from one stack to another.
        
        Args:
            from_stack (str): Name of the source stack
            to_stack (str): Name of the destination stack
        
        Returns:
            bool: True if move is possible, False otherwise
        """
        # Can't move if source stack is empty
        if not self.stacks[from_stack]:
            return False
        
        # Can't move if destination stack is already at target size
        if len(self.stacks[to_stack]) >= self.target_stack_size:
            return False
        
        return True
    
    def move_ball(self, from_stack: str, to_stack: str) -> None:
        """
        Move a single ball from one stack to another.
        
        Args:
            from_stack (str): Name of the source stack
            to_stack (str): Name of the destination stack
        
        Raises:
            ValueError: If move is not possible
        """
        if not self.can_move(from_stack, to_stack):
            raise ValueError(f"Cannot move ball from {from_stack} to {to_stack}")
        
        ball = self.stacks[from_stack].pop()
        self.stacks[to_stack].append(ball)
    
    def is_sorted(self) -> bool:
        """
        Check if all stacks have equal number of balls.
        
        Returns:
            bool: True if sorted, False otherwise
        """
        return all(len(stack) == self.target_stack_size for stack in self.stacks.values())
    
    def sort(self) -> List[Dict[str, List[str]]]:
        """
        Sort the stacks by moving balls between stacks.
        
        Returns:
            List[Dict[str, List[str]]]: Intermediate states of stacks during sorting
        """
        states = [dict(self.stacks)]
        
        while not self.is_sorted():
            # Find a stack with more than target balls
            for source_stack in self.stacks:
                # Check if source stack has more than target balls
                if len(self.stacks[source_stack]) > self.target_stack_size:
                    for dest_stack in self.stacks:
                        if source_stack != dest_stack and self.can_move(source_stack, dest_stack):
                            self.move_ball(source_stack, dest_stack)
                            states.append(dict(self.stacks))
                            break
                    break
        
        return states