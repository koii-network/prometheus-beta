import random

class Mountain:
    def __init__(self, name, height, latitude, longitude):
        """
        Initialize a Mountain object.
        
        :param name: Name of the mountain
        :param height: Height of the mountain in meters
        :param latitude: Latitude coordinate
        :param longitude: Longitude coordinate
        """
        self.name = name
        self.height = height
        self.latitude = latitude
        self.longitude = longitude

def create_mountain_range(num_peaks, min_height=1000, max_height=8848, 
                           latitude_range=(-90, 90), longitude_range=(-180, 180)):
    """
    Generate a list of mountain range objects with specified number of peaks.
    
    :param num_peaks: Number of peaks to generate in the mountain range
    :param min_height: Minimum height of mountains (default: 1000m)
    :param max_height: Maximum height of mountains (default: 8848m - Mt. Everest)
    :param latitude_range: Tuple of min and max latitude coordinates
    :param longitude_range: Tuple of min and max longitude coordinates
    :return: List of Mountain objects
    """
    if num_peaks < 0:
        raise ValueError("Number of peaks must be non-negative")
    
    mountain_names = [
        "Peak", "Summit", "Mountain", "Pinnacle", "Crest", 
        "Alpine", "Ridge", "Spire", "Vertex", "Zenith"
    ]
    
    mountain_range = []
    
    for i in range(num_peaks):
        # Generate a unique mountain name
        name = f"{random.choice(mountain_names)} {i+1}"
        
        # Randomly generate height within specified range
        height = random.randint(min_height, max_height)
        
        # Randomly generate latitude and longitude
        latitude = random.uniform(latitude_range[0], latitude_range[1])
        longitude = random.uniform(longitude_range[0], longitude_range[1])
        
        mountain = Mountain(name, height, latitude, longitude)
        mountain_range.append(mountain)
    
    return mountain_range