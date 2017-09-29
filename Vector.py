#coding=utf-8
import numpy as np

class Vector(object):
    def __init__(self):
        self._array = np.array([0., 0.],dtype=np.float64)

    @property
    def x(self):
        return self._array[0]

    @property
    def y(self):
        return self._array[1]

