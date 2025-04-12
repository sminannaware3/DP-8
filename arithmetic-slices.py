# DP Solution
# Time O(n)
# Space O(n)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        dp = [0] * n
        diff = nums[-1] - nums[-2]
        count = 0
        for i in range(n-3, -1, -1):
            currDiff = nums[i+1] - nums[i]
            if currDiff == diff:
                dp[i] = 1 + dp[i+1]
                count += dp[i]
            diff = currDiff
        return count

    
# Arithmatic solution
# Time O(n)
# Space O(1)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        count = 0
        res = 0
        diff = math.inf
        for i in range(1, n):
            currDiff = nums[i] - nums[i-1]
            if currDiff == diff:
                count += 1
            else:
                if count >= 2:
                    res += int((count-1) * (count-1+1) / 2) # Arithmatic progression n(n+1)/2
                count = 1
            diff = currDiff
        if count >= 2:
            res += int((count-1) * (count-1+1) / 2)
        return res
