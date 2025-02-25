import random

class Mountain:
    """
    Represents a mountain with specific attributes.
    
    Attributes:
        name (str): Name of the mountain
        height (float): Height of the mountain in meters
        location (str): Geographic location of the mountain
    """
    def __init__(self, name, height, location):
        """
        Initialize a Mountain object.
        
        Args:
            name (str): Name of the mountain
            height (float): Height of the mountain in meters
            location (str): Geographic location of the mountain
        """
        self.name = name
        self.height = height
        self.location = location

def create_mountain_range(num_peaks, region='Unknown'):
    """
    Generate a list of mountain objects with specified number of peaks.
    
    Args:
        num_peaks (int): Number of mountains to create in the range
        region (str, optional): Geographic region of the mountain range. Defaults to 'Unknown'.
    
    Returns:
        list: A list of Mountain objects
    
    Raises:
        ValueError: If num_peaks is negative or not an integer
    """
    # Validate input
    if not isinstance(num_peaks, int):
        raise TypeError("Number of peaks must be an integer")
    
    if num_peaks < 0:
        raise ValueError("Number of peaks cannot be negative")
    
    # List of possible mountain names and locations
    base_mountain_names = [
        'Peak Alpha', 'Peak Beta', 'Peak Gamma', 'Peak Delta', 'Peak Epsilon',
        'Summit One', 'Summit Two', 'Summit Three', 'Summit Four', 'Summit Five'
    ]
    
    # Generate mountain range
    mountain_range = []
    for i in range(num_peaks):
        # Handle cases where num_peaks exceeds base names
        if i < len(base_mountain_names):
            name = base_mountain_names[i]
        else:
            # Create unique names for additional peaks
            name = f"Peak {i + 1}"
        
        height = round(random.uniform(1000, 8000), 2)  # Heights between 1000m and 8000m
        
        # Create Mountain object
        mountain = Mountain(
            name=f"{name} ({region})", 
            height=height, 
            location=region
        )
        mountain_range.append(mountain)
    
    return mountain_range