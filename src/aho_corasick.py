from typing import List, Dict, Set

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        :param patterns: List of string patterns to search for
        """
        self.patterns = patterns
        self.goto = {}  # Goto function (transition table)
        self.fail = {}  # Failure function
        self.output = {}  # Output function (matching patterns)
        self._build_automaton()

    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton.
        """
        # Step 1: Build the goto function (Trie)
        self.goto = {}
        for pattern in self.patterns:
            current = 0
            for char in pattern:
                if current not in self.goto:
                    self.goto[current] = {}
                if char not in self.goto[current]:
                    next_state = len(self.goto)
                    self.goto[current][char] = next_state
                current = self.goto[current][char]
            
            # Mark the end of a pattern
            if current not in self.output:
                self.output[current] = set()
            self.output[current].add(pattern)

        # Step 2: Build the failure function
        self.fail = {0: 0}
        queue = []
        
        # Initialize first level of failure links
        for char, state in self.goto.get(0, {}).items():
            queue.append(state)
            self.fail[state] = 0

        # BFS to compute failure links
        while queue:
            current = queue.pop(0)
            
            # For each character from the current state
            for char, next_state in self.goto.get(current, {}).items():
                queue.append(next_state)
                
                # Find the longest proper suffix
                failure = self.fail[current]
                while failure > 0 and char not in self.goto.get(failure, {}):
                    failure = self.fail[failure]
                
                # Set the failure link
                if char in self.goto.get(failure, {}):
                    self.fail[next_state] = self.goto[failure][char]
                else:
                    self.fail[next_state] = 0
                
                # Aggregate output
                if next_state not in self.output:
                    self.output[next_state] = set()
                self.output[next_state].update(self.output.get(self.fail[next_state], set()))

    def find_matches(self, text: str) -> Dict[int, Set[str]]:
        """
        Find all matches of patterns in the given text.
        
        :param text: Input text to search in
        :return: Dictionary of match positions and corresponding patterns
        """
        matches = {}
        current = 0

        for i, char in enumerate(text):
            # Follow the goto and fail transitions
            while current > 0 and char not in self.goto.get(current, {}):
                current = self.fail[current]
            
            # Transition
            if char in self.goto.get(current, {}):
                current = self.goto[current][char]
            
            # Check for matches
            if current in self.output:
                for pattern in self.output[current]:
                    match_end = i + 1
                    match_start = match_end - len(pattern)
                    if match_start not in matches:
                        matches[match_start] = set()
                    matches[match_start].add(pattern)

        return matches