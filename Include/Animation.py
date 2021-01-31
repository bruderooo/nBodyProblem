import time

from matplotlib import pyplot as plt

from Include.World import World


class Animation(World):

    def __init__(self, no_bodies: int, file=None, dim: int = 2) -> None:
        super().__init__(no_bodies, file, dim)

    def start_simulation(self, cycles: int, duration: float = 0):
        plt.ion()
        fig, ax = plt.subplots()
        point, = ax.plot([], [], 'ro')

        ax.set_xlim(-1000, 1000)
        ax.set_ylim(-1000, 1000)

        for _ in range(cycles):
            self.one_epoch()

            tmp = self.get_all_positions().T
            x, y = tmp

            point.set_xdata(x)
            point.set_ydata(y)

            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(0.01)
