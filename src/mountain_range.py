import random

class Mountain:
    def __init__(self, name, height, location):
        """
        Initialize a Mountain object.
        
        :param name: Name of the mountain
        :param height: Height of the mountain in meters
        :param location: Geographic location of the mountain
        """
        self.name = name
        self.height = height
        self.location = location

def create_mountain_range(num_peaks):
    """
    Generate a list of mountain range objects with specified number of peaks.
    
    :param num_peaks: Number of peaks to generate
    :return: List of Mountain objects
    :raises ValueError: If num_peaks is less than 1
    """
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    # List of sample mountain names and locations
    mountain_names = [
        "Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", 
        "Cho Oyu", "Dhaulagiri", "Manaslu", "Nanga Parbat", "Annapurna"
    ]
    locations = [
        "Himalayas", "Karakoram", "Alps", "Andes", "Rockies", 
        "Alaska Range", "Patagonian Andes", "Cascade Range", "Transantarctic Mountains", "Ural Mountains"
    ]
    
    mountain_range = []
    used_names = set()
    
    for _ in range(num_peaks):
        # Ensure unique mountain names
        while True:
            name = random.choice(mountain_names)
            if name not in used_names:
                used_names.add(name)
                break
        
        # Generate a random height between 4000 and 9000 meters
        height = random.randint(4000, 9000)
        
        # Choose a random location
        location = random.choice(locations)
        
        mountain = Mountain(name, height, location)
        mountain_range.append(mountain)
    
    return mountain_range