from __future__ import annotations

from typing import List, Union

import numpy as np
from numpy import G, ndarray
from numpy.linalg import norm


class Body:

    def __init__(self, mass: Union[float, None],
                 position: Union[List[float], ndarray[float]] = None,
                 velocity: Union[List[float], ndarray[float]] = None,
                 random_val=False, dim=2) -> None:

        self.mass = mass if mass is not None else np.random.uniform(-10, 10)
        self.acceleration = np.zeros(dim)

        if random_val or (position is not None and velocity is not None):
            self.position = np.random.uniform(-10, 10, dim) if random_val else position
            self.velocity = np.random.uniform(-10, 10, dim) if random_val else velocity

            self.new_position = self.position
            self.new_velocity = self.velocity

    def distance_to(self, body: Body):
        # np.linalg.norm(A - B)
        # this is euclidean distance A to B
        return np.linalg.norm(self.position - body.position)

    def force_to(self, body: Body):
        return (G * self.mass * body.mass) / self.distance_to(body) ** 2

    def compute(self, body: Body):
        self.new_position = self.position + (self.velocity + 0.5 * self.acceleration)
        self.new_velocity = self.velocity + self.acceleration

        distance_abs = np.absolute(self.position - body.position)
        self.acceleration += (G * body.mass / pow(distance_abs, 3)) * distance_abs

    def update(self):
        self.position = self.new_position
        self.velocity = self.new_velocity

    def __eq__(self, other):
        return hex(id(self)) == hex(id(other))
