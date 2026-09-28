# LeetCode 1480 - Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        total = 0
        result = []

        for i in nums:
            total += i
            result.append(total)

        return result
