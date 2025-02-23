import random
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Peak:
    """
    Represents a mountain peak with name and height attributes.
    
    Attributes:
        name (str): Name of the peak
        height (float): Height of the peak in meters
    """
    name: str
    height: float

@dataclass
class MountainRange:
    """
    Represents a mountain range with multiple peaks.
    
    Attributes:
        name (str): Name of the mountain range
        peaks (List[Peak]): List of peaks in the mountain range
    """
    name: str
    peaks: List[Peak]

def create_mountain_range(
    num_peaks: int, 
    range_name: Optional[str] = None, 
    min_height: float = 1000.0, 
    max_height: float = 8848.0
) -> MountainRange:
    """
    Generate a mountain range with a specified number of peaks.
    
    Args:
        num_peaks (int): Number of peaks to generate
        range_name (Optional[str], optional): Name of the mountain range. 
                                              Defaults to a random name if not provided.
        min_height (float, optional): Minimum peak height in meters. Defaults to 1000.0.
        max_height (float, optional): Maximum peak height in meters. Defaults to 8848.0.
    
    Raises:
        ValueError: If num_peaks is less than 1
        ValueError: If min_height is greater than or equal to max_height
    
    Returns:
        MountainRange: A mountain range with generated peaks
    """
    # Validate inputs
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    if min_height >= max_height:
        raise ValueError("Minimum height must be less than maximum height")
    
    # Generate range name if not provided
    if range_name is None:
        range_name = random.choice([
            "Alpine Ridge", "Volcanic Mountains", "Granite Peaks", 
            "Snowy Range", "Rocky Highlands"
        ])
    
    # Generate peaks
    peaks = []
    peak_names = [
        "Summit", "Crown", "Peak", "Pinnacle", "Apex", 
        "Crest", "Vertex", "Spire", "Point", "Ridge"
    ]
    
    for i in range(num_peaks):
        # Generate unique peak name
        name = f"{random.choice(peak_names)} {i+1}"
        
        # Generate random height within specified range
        height = round(random.uniform(min_height, max_height), 2)
        
        peaks.append(Peak(name=name, height=height))
    
    return MountainRange(name=range_name, peaks=peaks)