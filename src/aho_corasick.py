from typing import List, Dict, Set, Tuple
from collections import deque

class AhoCorasick:
    """
    Aho-Corasick algorithm implementation for efficient multiple string matching.
    
    This class builds a finite state machine that can simultaneously match 
    multiple patterns in a given text with O(n+m+z) time complexity, 
    where n is the text length, m is the total length of all patterns, 
    and z is the number of matches.
    """
    
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick automaton.
        
        Args:
            patterns (List[str]): List of patterns to match
        
        Raises:
            ValueError: If patterns list is empty
        """
        if not patterns:
            raise ValueError("At least one pattern must be provided")
        
        self.patterns = patterns
        self.goto = {}  # Goto transitions
        self.fail = {}  # Failure links
        self.output = {}  # Output matches
        
        self._build_automaton()
    
    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton.
        Builds goto transitions, failure links, and output matches.
        """
        # Initialize goto transitions for root state
        self.goto[0] = {}
        
        # Build goto transitions
        state = 0
        for pattern in self.patterns:
            current = 0
            for char in pattern:
                # Create new state if transition doesn't exist
                if current not in self.goto:
                    self.goto[current] = {}
                if char not in self.goto[current]:
                    state += 1
                    self.goto[current][char] = state
                    self.goto[state] = {}
                current = self.goto[current][char]
            
            # Mark end of pattern
            if current not in self.output:
                self.output[current] = []
            self.output[current].append(pattern)
        
        # Build failure links using BFS
        self.fail[0] = 0
        queue = deque()
        
        # Add first-level states to queue
        for char, state in self.goto[0].items():
            queue.append(state)
            self.fail[state] = 0
        
        # Build failure links
        while queue:
            current = queue.popleft()
            
            for char, next_state in self.goto[current].items():
                queue.append(next_state)
                
                # Find longest proper suffix
                state = self.fail[current]
                while state > 0 and char not in self.goto[state]:
                    state = self.fail[state]
                
                # Set failure link
                if char in self.goto[state]:
                    self.fail[next_state] = self.goto[state][char]
                else:
                    self.fail[next_state] = 0
                
                # Merge outputs from failure links
                if self.fail[next_state] in self.output:
                    if next_state not in self.output:
                        self.output[next_state] = []
                    self.output[next_state].extend(self.output[self.fail[next_state]])
    
    def find_matches(self, text: str) -> List[Tuple[int, str]]:
        """
        Find all matches of patterns in the given text.
        
        Args:
            text (str): Input text to search for patterns
        
        Returns:
            List[Tuple[int, str]]: List of tuples containing match index and matched pattern
        
        Raises:
            TypeError: If input is not a string
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        matches = []
        current = 0
        
        for i, char in enumerate(text):
            # Follow goto and failure transitions
            while current > 0 and char not in self.goto[current]:
                current = self.fail[current]
            
            # Move to next state
            if char in self.goto[current]:
                current = self.goto[current][char]
            
            # Check for matches at current state
            if current in self.output:
                for pattern in self.output[current]:
                    matches.append((i - len(pattern) + 1, pattern))
        
        return matches