from __future__ import annotations

from typing import List
import numpy as np

from Include.Body import Body


class World:

    def __init__(self, bodies: int, cycles: int, file=None) -> None:
        self.bodies: List[Body] = []
        # for i in range(bodies):
        #     self.bodies += [Body()]
