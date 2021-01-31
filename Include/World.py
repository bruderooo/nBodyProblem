from __future__ import annotations

import time
from typing import List
import numpy as np

from Include.Body import Body


class World:

    def __init__(self, no_bodies: int, file=None) -> None:
        self.bodies: List[Body] = []
        if file is None:
            for _ in range(no_bodies):
                self.bodies += [Body(1, random_val=True)]
        else:
            for _ in range(no_bodies):
                # self.bodies += [Body()]
                pass

    def start_simulation(self, cycles: int, duration: float = 0):
        for _ in range(cycles):
            self.one_epoch()
            time.sleep(duration)

    def one_epoch(self):
        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    body1.compute(body2)

        for body in self.bodies:
            body.update()
