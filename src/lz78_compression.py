class LZ78Compressor:
    def __init__(self):
        # Initialize dictionary with 0-index for empty entry
        self.dictionary = {0: ''}
        self.next_code = 1

    def compress(self, input_string):
        """
        Implement LZ78 compression algorithm
        
        Args:
            input_string (str): The input string to compress
        
        Returns:
            list: A list of tuples (index, character) representing compressed data
        """
        if not input_string:
            return []

        compressed = []
        current_sequence = ''

        for char in input_string:
            # Try to find the longest match in the dictionary
            new_sequence = current_sequence + char
            found = False

            for index, value in self.dictionary.items():
                if value == new_sequence:
                    current_sequence = new_sequence
                    found = True
                    break

            # If no match found, add to dictionary and reset current sequence
            if not found:
                # Find the index of the longest prefix
                prefix_index = 0
                for index, value in self.dictionary.items():
                    if value == current_sequence:
                        prefix_index = index
                        break

                # Add to dictionary and compressed output
                compressed.append((prefix_index, char))
                self.dictionary[self.next_code] = new_sequence
                self.next_code += 1
                current_sequence = ''

        # Handle any remaining sequence
        if current_sequence:
            for index, value in self.dictionary.items():
                if value == current_sequence:
                    compressed.append((index, ''))
                    break

        return compressed

    def decompress(self, compressed_data):
        """
        Implement LZ78 decompression algorithm
        
        Args:
            compressed_data (list): Compressed data as list of tuples (index, character)
        
        Returns:
            str: Decompressed original string
        """
        if not compressed_data:
            return ''

        # Reset dictionary for decompression
        dictionary = {0: ''}
        next_code = 1
        decompressed = []

        for index, char in compressed_data:
            # Retrieve the string from dictionary based on index
            prefix = dictionary.get(index, '')
            
            # Construct new string
            current_string = prefix + char

            # Add to dictionary
            dictionary[next_code] = current_string
            next_code += 1

            # Add to output
            decompressed.append(current_string)

        return ''.join(decompressed)