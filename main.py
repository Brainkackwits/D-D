import os
import time
class statics()
    def __init__(self):
        self.path = os.path.abspath(__file__)
        pass

print(os.path.abspath(__file__))
