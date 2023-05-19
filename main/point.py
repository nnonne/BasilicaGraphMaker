import itertools

class Points:
    def __init__(self, n):
        self.n = n
        self.count = n**2
        self.points, self.x = self.make_points()
        self.y = [0]*self.count

    def make_points(self):
        labels = [''.join(seq) for seq in itertools.product('01', repeat=self.n)]
        xs = [x for x in range(2**(self.n-1)*(-70), 2**(self.n-1)*70, 70)]
        return labels, xs

    def find_point(self, label):
        return self.x[self.points.index(label)]
