import math as m
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = 2**31
        n = len(points)
        j = -1
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                distance = m.sqrt((points[i][0]-x)**2 + (points[i][1]-y)**2)
                if distance < dist:
                    dist = distance
                    j = i            
        return j
