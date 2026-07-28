class CountSquares:

    def __init__(self):
        self.pts = {}   # (x, y): number of points at (x, y)

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        if p not in self.pts:
            self.pts[p] = 0
        self.pts[p] += 1

    def count(self, point: List[int]) -> int:
        # Iterate through each unique coordinate to find the valid diagonal coordinate of point.
        px, py = point
        res = 0
        for x, y in self.pts:
            if x == px or y == py or abs(px - x) != abs(py - y):
                continue
            
            res += self.pts.get((x, y), 0) * self.pts.get((px, y), 0) * self.pts.get((x, py), 0)
        
        return res