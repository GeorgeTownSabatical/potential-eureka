"""
Filter utilities (bandpass, highpass, etc).
"""

def bandpass_filter(data, fs, f_low, f_high=None, order=4):
    """
    Apply a bandpass filter to data.

    Args:
        data: np.ndarray, input signal
        fs: int, sampling frequency
        f_low: float, low cutoff frequency
        f_high: float, high cutoff frequency (optional)
        order: int, filter order

    Returns:
        np.ndarray: filtered data
    """
    # Placeholder for actual implementation
    return data
