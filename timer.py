import time

class Timer:
    
    def __init__(self, value = 0):
        self.start = time.time()
        self.set(value)

    def get (self) -> float:
        return time.time() - self.start
    
    def set (self, value : float):
        self.start = time.time() - value

    def __str__(self):
        value = self.get()
        self.sec = str(int(value))