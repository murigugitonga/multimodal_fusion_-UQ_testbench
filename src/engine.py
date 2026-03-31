import numpy as np

class UQKalmanFilter:
    def __init__(self, q=0.1, r=1.0):
        self.Q = q
        self.R = r
        self.x =  0.0
        self.p = 1.0
        self.threshold = 3.0

    def predict(self):
        self.P = self.P + self.Q
        return self.x
    
    def update(self, z, r_current):
        y = z - self.x
        S = self.P + r_current

        nis = (y**2)/ S
        is_spoofed = nis > self.threshold

        if not is_spoofed:
            K = self.P / S
            self.x = self.x + K * y
            self.P = (1 - K) * self.P

        return self.x, is_spoofed, nis