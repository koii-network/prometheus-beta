from typing import List, Dict, Tuple
from collections import deque

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match
        
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
        # Construct the initial goto transitions (trie)
        for pattern in self.patterns:
            current = 0
            for char in pattern:
                if current not in self.goto:
                    self.goto[current] = {}
                if char not in self.goto[current]:
                    state = len(self.goto)
                    self.goto[current][char] = state
                current = self.goto[current][char]
            
            # Mark the end of a pattern
            if current not in self.output:
                self.output[current] = []
            if pattern not in self.output[current]:
                self.output[current].append(pattern)

        # Construct failure links using BFS
        self.fail = {0: 0}
        queue = deque()

        # Initialize first level failure links
        for char, state in self.goto.get(0, {}).items():
            queue.append(state)
            self.fail[state] = 0

        # BFS to construct failure links
        while queue:
            current = queue.popleft()
            
            # Check each possible character transition
            for char, next_state in self.goto.get(current, {}).items():
                queue.append(next_state)
                
                # Find the longest proper suffix link
                failure = self.fail[current]
                while failure > 0 and char not in self.goto.get(failure, {}):
                    failure = self.fail[failure]
                
                # Set failure link
                if failure > 0 and char in self.goto.get(failure, {}):
                    self.fail[next_state] = self.goto[failure][char]
                else:
                    self.fail[next_state] = 0

                # Merge outputs from failure links
                if self.fail[next_state] in self.output:
                    if next_state not in self.output:
                        self.output[next_state] = []
                    for pattern in self.output[self.fail[next_state]]:
                        if pattern not in self.output[next_state]:
                            self.output[next_state].append(pattern)

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Search for patterns in the given text
        
        :param text: Input text to search
        :return: List of tuples (index, matched_pattern)
        """
        results = []
        current = 0

        for i, char in enumerate(text):
            # Follow goto and failure transitions
            while current > 0 and char not in self.goto.get(current, {}):
                current = self.fail[current]

            # Move to next state if possible
            if current in self.goto and char in self.goto[current]:
                current = self.goto[current][char]
            
            # Check for matches
            state = current
            while state > 0:
                if state in self.output:
                    for pattern in self.output[state]:
                        # Find the start index of the match
                        start_index = max(0, i - len(pattern) + 1)
                        match_tuple = (start_index, pattern)
                        if match_tuple not in results:
                            results.append(match_tuple)
                state = self.fail[state]

        return results