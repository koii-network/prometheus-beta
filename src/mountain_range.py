import random

class Mountain:
    def __init__(self, name, height, latitude, longitude):
        """
        Initialize a Mountain object with basic characteristics.
        
        :param name: Name of the mountain
        :param height: Height of the mountain in meters
        :param latitude: Latitude coordinate
        :param longitude: Longitude coordinate
        """
        self.name = name
        self.height = height
        self.latitude = latitude
        self.longitude = longitude

def create_mountain_range(num_peaks):
    """
    Generate a list of mountain range objects with the specified number of peaks.
    
    :param num_peaks: Number of peaks to generate in the mountain range
    :return: List of Mountain objects
    :raises ValueError: If num_peaks is less than 1
    """
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    mountain_names = [
        "Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", 
        "Cho Oyu", "Dhaulagiri", "Manaslu", "Nanga Parbat", "Annapurna"
    ]
    
    mountain_range = []
    for i in range(num_peaks):
        # Randomly select a mountain name, ensuring no duplicates
        name = random.choice([n for n in mountain_names if n not in [m.name for m in mountain_range]])
        
        # Generate random height between 6000 and 8848 (max height of Everest)
        height = random.randint(6000, 8848)
        
        # Generate random latitude and longitude (roughly in Himalayan region)
        latitude = random.uniform(26.0, 30.0)
        longitude = random.uniform(86.0, 88.0)
        
        mountain = Mountain(name, height, latitude, longitude)
        mountain_range.append(mountain)
    
    return mountain_range