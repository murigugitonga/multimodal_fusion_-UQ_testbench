import numpy as np

def get_sensor_reading(true_pos, noise_std, spoof = False):
    if spoof:
        # A spoofer provides a false, low variance signal to trick the filter into trusting it
        return 50.0 + np.random.normal(0, 0.01)
    return true_pos + np.random.normal(0, noise_std)