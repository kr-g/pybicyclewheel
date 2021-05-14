import numpy as np


class Rim(object):
    def __init__(self, erd=598):
        self.erd = erd
        self.radius = erd / 2.0

    def __repr__(self):
        return str(self.__dict__)

    def vec(self):
        """this vector points from the center of the wheel to the rim"""
        return np.array([0, self.radius, 0])
