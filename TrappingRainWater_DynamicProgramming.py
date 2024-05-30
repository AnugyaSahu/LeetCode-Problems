
"""
https://leetcode.com/problems/trapping-rain-water/description/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        rain_trapped = 0

        left_max, right_max = list(height), list(height[::-1])


        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], left_max[i])

        for j in range(1, len(height)):
            right_max[j] = max(right_max[j-1], right_max[j])

        right_max = right_max[::-1]

        for i, bar_height in enumerate(height):
            rain = min(left_max[i], right_max[i]) - bar_height

            if rain > 0:
                rain_trapped += rain

        return rain_trapped

