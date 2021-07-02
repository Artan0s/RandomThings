# from facebook page MetaMath, post https://www.facebook.com/groups/605013976789733/posts/839147126709749

import numpy as np
import matplotlib.pyplot as plt


class Polygon():
    def __init__(self, sides, side_length=2):
        self.sides = sides
        self.segments = sides//2
        self.length = side_length
        self.theta = 2*np.pi/sides
        self.H = (self.length/2) / np.sin(self.theta / 2)
        self.seg_lengths = None
        self.sum_segs = 0

    def calc_segments(self):
        heights = np.zeros(self.segments+1)
        for n in range(self.segments + 1):
            heights[n] = self.H*(1 - np.cos(n*self.theta))
        seg_lengths = np.zeros(self.segments)
        for n in range(self.segments):
            seg_lengths[n] = heights[n+1] - heights[n]
        sum_segs = np.sum(seg_lengths**2)
        self.seg_lengths = seg_lengths
        self.sum_segs = sum_segs
        print(self.sides, sum_segs)
        return np.round(sum_segs)


inf = 3
sup = int(1e4)
a0 = range(inf, sup+1)
a1 = 0*np.array(a0)
for n in a0:
    poly = Polygon(n)
    a1[n-inf] = poly.calc_segments()

plt.plot(a1-a0)
plt.show()