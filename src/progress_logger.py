import sys
import time

class ProgressBar:
    """
    A dynamic progress bar logger that updates in-place on the console.

    Attributes:
        total (int): Total number of steps to complete
        prefix (str): Prefix text before the progress bar
        suffix (str): Suffix text after the progress bar
        decimals (int): Number of decimal places for percentage
        length (int): Character length of the progress bar
        fill (str): Character used to fill the progress bar
        print_end (str): End character (default is carriage return to overwrite)
    """
    def __init__(self, total, prefix='Progress:', suffix='Complete', 
                 decimals=1, length=50, fill='█', print_end='\r'):
        """
        Initialize the progress bar.

        Args:
            total (int): Total number of iterations expected
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.current = 0

    def update(self, current=None):
        """
        Update the progress bar.

        Args:
            current (int, optional): Current iteration. If None, increments by 1.
        
        Raises:
            ValueError: If current iteration exceeds total iterations
        """
        # Increment if no current value provided
        if current is None:
            self.current += 1
        else:
            # Validate input
            if current < 0:
                raise ValueError("Current iteration cannot be negative")
            if current > self.total:
                raise ValueError(f"Current iteration cannot exceed total ({self.total})")
            self.current = current

        # Calculate percentage and length of filled bar
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.current / float(self.total)))
        filled_length = int(self.length * self.current // self.total)
        
        # Create the bar
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # Print the progress bar
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end=self.print_end)
        
        # Print a newline when complete
        if self.current >= self.total:
            print()

    def __iter__(self):
        """
        Make the progress bar iterable.

        Returns:
            ProgressBar: The progress bar instance
        """
        return self

    def __next__(self):
        """
        Support iteration protocol.

        Returns:
            int: Current iteration number

        Raises:
            StopIteration: When all iterations are complete
        """
        if self.current >= self.total:
            raise StopIteration
        
        self.update()
        return self.current


def log_with_progress(iterable, prefix='Progress:', **kwargs):
    """
    Decorator/wrapper to add progress bar to any iterable.

    Args:
        iterable (iterable): The iterable to track progress for
        prefix (str, optional): Prefix for progress bar
        **kwargs: Additional ProgressBar configuration options

    Returns:
        ProgressBar: A progress bar wrapping the input iterable
    """
    return ProgressBar(len(iterable), prefix=prefix, **kwargs)