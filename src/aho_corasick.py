from typing import List, Dict, Tuple
from collections import deque

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        :param patterns: List of strings to search for
        """
        self.patterns = patterns
        self.goto = {}  # Goto transitions
        self.fail = {}  # Failure links
        self.output = {}  # Output matches
        self._build_automaton()

    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton
        """
        # Build the initial trie
        for pattern in self.patterns:
            current = 0
            for char in pattern:
                if current not in self.goto:
                    self.goto[current] = {}
                if char not in self.goto[current]:
                    self.goto[current][char] = len(self.goto)
                current = self.goto[current][char]
            
            # Mark the end of a pattern
            if current not in self.output:
                self.output[current] = []
            self.output[current].append(pattern)

        # Build failure links using BFS
        self.fail = {0: 0}
        queue = deque()

        # Initialize first level failure links
        for char, state in self.goto.get(0, {}).items():
            queue.append(state)
            self.fail[state] = 0

        # BFS to construct failure links
        while queue:
            state = queue.popleft()
            for char, next_state in self.goto.get(state, {}).items():
                queue.append(next_state)
                
                # Find the longest proper suffix
                failure = self.fail[state]
                while failure > 0 and char not in self.goto.get(failure, {}):
                    failure = self.fail[failure]
                
                # Set failure link
                if failure in self.goto and char in self.goto[failure]:
                    self.fail[next_state] = self.goto[failure][char]
                else:
                    self.fail[next_state] = 0
                
                # Combine output with failure link's output
                if next_state not in self.output:
                    self.output[next_state] = []
                if self.fail[next_state] in self.output:
                    self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Search for patterns in the given text.
        
        :param text: Input text to search
        :return: List of tuples (index, matched_pattern)
        """
        results = []
        current = 0

        for i, char in enumerate(text):
            # Follow goto and failure links
            while current > 0 and char not in self.goto.get(current, {}):
                current = self.fail[current]

            # Move to next state
            if current in self.goto and char in self.goto[current]:
                current = self.goto[current][char]
            
            # Check for matches
            if current in self.output:
                for pattern in self.output[current]:
                    results.append((i - len(pattern) + 1, pattern))

        return results