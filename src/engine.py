import numpy as np

class UQKalmanFilter:
    def __init__(self, q=0.1, r=1.0):
        self.Q = q
        self.R = r
        self.x =  0.0
        self.P = 1.0
        self.threshold = 3.0 # statistical gate

    def predict(self):
        self.P = self.P + self.Q
        return self.x
    
    def update(self, z, r_current):
        # Innovation (Residual)
        y = z - self.x
        S = self.P + r_current

        nis = (y**2)/ S
        is_spoofed = nis > self.threshold
        # Uncertainity Quantification: Check if statistical outlier
        # Check nis( Normalized Innovation Squared)
        if not is_spoofed:
            # Standard Kalman update
            K = self.P / S
            self.x = self.x + K * y
            self.P = (1 - K) * self.P

        return self.x, is_spoofed, nis