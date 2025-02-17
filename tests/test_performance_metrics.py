import pytest
from src.performance_metrics import log_browser_performance_metrics

def test_performance_metrics_structure():
    """
    Test that the performance metrics have the expected structure
    """
    metrics = log_browser_performance_metrics()
    
    # Check that the returned object is a dictionary
    assert isinstance(metrics, dict)
    
    # Check for key sections
    assert "timing" in metrics
    assert "navigation" in metrics
    assert "render_metrics" in metrics

def test_performance_metrics_types():
    """
    Test that the metrics have the correct data types
    """
    metrics = log_browser_performance_metrics()
    
    # Check timing types
    assert isinstance(metrics["timing"], dict)
    assert all(isinstance(x, int) for x in metrics["timing"].values())
    
    # Check navigation types
    assert isinstance(metrics["navigation"], dict)
    assert isinstance(metrics["navigation"]["type"], str)
    
    # Check render metrics types
    assert isinstance(metrics["render_metrics"], dict)
    assert all(isinstance(x, (int, float)) for x in metrics["render_metrics"].values())

def test_performance_metrics_values():
    """
    Test that the metrics have reasonable values
    """
    metrics = log_browser_performance_metrics()
    
    # Navigation start should be greater than 0
    assert metrics["timing"]["navigationStart"] > 0
    
    # Load times should be non-negative
    render_metrics = metrics["render_metrics"]
    assert render_metrics["total_load_time"] >= 0
    assert render_metrics["dom_load_time"] >= 0
    assert render_metrics["first_contentful_paint"] >= 0