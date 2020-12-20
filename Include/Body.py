from __future__ import annotations

from typing import List

from numpy import G
import numpy as np
import matplotlib.pyplot as plt

from Include.Vector import Vector


class Body:

    def __init__(self, mass: float, position: List[float], velocity: List[float]) -> None:
        self.mass = mass
        self.position = Vector(position)
        self.velocity = Vector(velocity)
        self.acceleration = Vector(np.zeros(len(velocity)))

    def distance_to(self, body: Body):
        return self.position.euclidean_distance(body.position)

    def force_to(self, body: Body):
        return (G * self.mass * body.mass) / self.distance_to(body) ** 2
