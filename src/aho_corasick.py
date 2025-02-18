from typing import List, Dict, Tuple

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        :param patterns: List of strings to search for
        """
        self.patterns = patterns
        self.goto = {}  # Goto function (transition table)
        self.fail = {}  # Failure function 
        self.output = {}  # Output function (stores matched patterns)
        self._build_automaton()

    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton.
        """
        # Initialize goto function with root
        self.goto = {0: {}}
        self.fail = {0: 0}
        self.output = {0: []}
        state_counter = 1

        # Build the initial trie
        for pattern in self.patterns:
            current_state = 0
            for char in pattern:
                if current_state not in self.goto:
                    self.goto[current_state] = {}
                
                if char not in self.goto[current_state]:
                    self.goto[current_state][char] = state_counter
                    self.goto[state_counter] = {}
                    self.fail[state_counter] = 0
                    self.output[state_counter] = []
                    state_counter += 1
                
                current_state = self.goto[current_state][char]
            
            # Mark the end of a pattern
            self.output[current_state].append(pattern)

        # Build failure and goto function
        queue = []
        for char, state in self.goto[0].items():
            queue.append(state)
            self.fail[state] = 0

        while queue:
            state = queue.pop(0)
            for char, next_state in self.goto[state].items():
                queue.append(next_state)
                
                # Find the longest proper suffix
                failure_state = self.fail[state]
                while (failure_state != 0 and 
                       char not in self.goto[failure_state]):
                    failure_state = self.fail[failure_state]
                
                # Set failure link
                if char in self.goto[failure_state]:
                    self.fail[next_state] = self.goto[failure_state][char]
                else:
                    self.fail[next_state] = 0
                
                # Combine outputs
                self.output[next_state].extend(
                    self.output[self.fail[next_state]]
                )

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Search for all pattern matches in the given text.
        
        :param text: Input text to search
        :return: List of tuples (start_index, matched_pattern)
        """
        results = []
        current_state = 0

        for i, char in enumerate(text):
            # Follow goto and failure transitions
            while (current_state != 0 and 
                   char not in self.goto[current_state]):
                current_state = self.fail[current_state]
            
            # Move to next state
            if char in self.goto[current_state]:
                current_state = self.goto[current_state][char]
            
            # Check for matches
            for pattern in self.output[current_state]:
                start_index = i - len(pattern) + 1
                results.append((start_index, pattern))
        
        return results