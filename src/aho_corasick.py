from typing import List, Dict, Tuple

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        :param patterns: List of strings to search for
        """
        self.patterns = patterns
        self.goto = {}  # Goto function (transitions)
        self.fail = {}  # Failure function
        self.output = {}  # Output function (matched patterns)
        self._build_automaton()

    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton.
        """
        # Construct the goto function (trie)
        self.goto = {0: {}}
        state_counter = 1

        for pattern in self.patterns:
            current_state = 0
            for char in pattern:
                if current_state not in self.goto or char not in self.goto[current_state]:
                    self.goto[state_counter] = {}
                    self.goto[current_state][char] = state_counter
                    current_state = state_counter
                    state_counter += 1
                else:
                    current_state = self.goto[current_state][char]
            
            # Mark the final state with the matched pattern
            if current_state not in self.output:
                self.output[current_state] = []
            self.output[current_state].append(pattern)

        # Construct the failure function
        self.fail = {state: 0 for state in range(state_counter)}
        queue = []

        # Set up failure function for first level
        for char, state in self.goto[0].items():
            queue.append(state)

        while queue:
            current_state = queue.pop(0)
            for char, next_state in self.goto[current_state].items():
                queue.append(next_state)
                
                # Find the longest proper suffix
                failure_state = self.fail[current_state]
                while failure_state > 0 and char not in self.goto[failure_state]:
                    failure_state = self.fail[failure_state]
                
                if failure_state > 0 and char in self.goto[failure_state]:
                    self.fail[next_state] = self.goto[failure_state][char]
                else:
                    self.fail[next_state] = 0

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Search for all patterns in the given text.
        
        :param text: Input text to search
        :return: List of tuples (start_index, matched_pattern)
        """
        results = []
        current_state = 0

        for i, char in enumerate(text):
            # Move in the automaton
            while current_state > 0 and char not in self.goto[current_state]:
                current_state = self.fail[current_state]
            
            if char in self.goto[current_state]:
                current_state = self.goto[current_state][char]
            
            # Check for matches
            state = current_state
            while state > 0:
                if state in self.output:
                    for pattern in self.output[state]:
                        results.append((i - len(pattern) + 1, pattern))
                state = self.fail[state]

        return results