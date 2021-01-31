from __future__ import annotations

import time
from typing import List
import numpy as np

from Include.Body import Body


class World:

    def __init__(self, no_bodies: int, file=None, dim: int = 2) -> None:
        self.bodies: List[Body] = []
        if file is None:
            for _ in range(no_bodies):
                self.bodies += [Body(10000000, random_val=True, dim=dim)]
        else:
            for _ in range(no_bodies):
                # self.bodies += [Body()]
                pass

        self.epoch = 0

    def start_simulation(self, cycles: int, duration: float = 0):
        for _ in range(cycles):
            self.one_epoch()
            print(self)
            time.sleep(duration)

    def one_epoch(self):
        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    body1.compute(body2)

        for body in self.bodies:
            body.update()

        self.epoch += 1

    def get_all_positions(self):
        all_positions = []

        for body in self.bodies:
            all_positions += [body.position]

        return np.array(all_positions)

    def __str__(self) -> str:
        text = f"Epoka {self.epoch}: "
        for body in self.bodies:
            text += f"{body.position} | "
        return text
