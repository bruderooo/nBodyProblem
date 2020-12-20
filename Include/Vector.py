from __future__ import annotations

import numpy as np


class Vector:

    def __init__(self, xyz) -> None:
        self.xyz = np.array(xyz)

    def __add__(self, vector: Vector):
        self.xyz = self.xyz + vector.xyz

    def __sub__(self, vector: Vector):
        self.xyz = self.xyz - vector.xyz

    def mod(self):
        return self.euclidean_distance(Vector(np.zeros(self.xyz.shape)))

    def euclidean_distance(self, vector: Vector):
        r = 0
        for one, two in zip(self.xyz, vector.xyz):
            r += (one - two) ** 2
        return r ** 0.5
