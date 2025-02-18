from typing import List, Dict, Set, Tuple
from collections import deque

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to search for.
        
        :param patterns: List of strings to search for in a text
        """
        self.patterns = patterns
        self.goto = {}  # Goto function (transitions)
        self.fail = {}  # Failure function 
        self.output = {}  # Output function (matched patterns)
        self._build_automaton()

    def _build_automaton(self):
        """
        Build the Aho-Corasick automaton with goto, fail, and output functions.
        """
        # Initialize goto function with root state
        self.goto[0] = {}
        
        # State counter, starts at 1 as 0 is the root
        state_counter = 1
        
        # Construct goto function (trie)
        for pattern in self.patterns:
            current_state = 0
            for char in pattern:
                if current_state not in self.goto:
                    self.goto[current_state] = {}
                
                if char not in self.goto[current_state]:
                    self.goto[current_state][char] = state_counter
                    state_counter += 1
                
                current_state = self.goto[current_state][char]
            
            # Mark end of pattern
            if current_state not in self.output:
                self.output[current_state] = set()
            self.output[current_state].add(pattern)
        
        # Construct failure function using BFS
        self.fail[0] = 0
        queue = deque()
        
        # Add all direct children of root to the queue
        for char, state in self.goto[0].items():
            queue.append(state)
            self.fail[state] = 0
        
        # BFS to build failure function
        while queue:
            current_state = queue.popleft()
            
            # Check all possible character transitions from current state
            for char, next_state in list(self.goto.get(current_state, {}).items()):
                queue.append(next_state)
                
                # Find the longest proper suffix
                fail_state = self.fail[current_state]
                while fail_state > 0 and char not in self.goto.get(fail_state, {}):
                    fail_state = self.fail[fail_state]
                
                # Set failure function
                if char in self.goto.get(fail_state, {}):
                    self.fail[next_state] = self.goto[fail_state][char]
                else:
                    self.fail[next_state] = 0
                
                # Combine output sets
                if self.fail[next_state] in self.output:
                    if next_state not in self.output:
                        self.output[next_state] = set()
                    self.output[next_state].update(self.output[self.fail[next_state]])

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Search for patterns in the given text.
        
        :param text: Input text to search
        :return: List of tuples (index, pattern) where patterns are found
        """
        results = []
        current_state = 0
        
        for i, char in enumerate(text):
            # Follow goto and fail transitions
            while current_state > 0 and char not in self.goto.get(current_state, {}):
                current_state = self.fail[current_state]
            
            # Move to next state
            if char in self.goto.get(current_state, {}):
                current_state = self.goto[current_state][char]
            
            # Check for matches
            state = current_state
            while state > 0:
                if state in self.output:
                    for pattern in self.output[state]:
                        results.append((i - len(pattern) + 1, pattern))
                state = self.fail[state]
        
        return results