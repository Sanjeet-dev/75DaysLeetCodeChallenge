class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        fix_size_sum = sum(nums[:k])
        max_sum = fix_size_sum

        for i in range(k, len(nums)):
            fix_size_sum += nums[i]
            fix_size_sum -= nums[i-k]

            max_sum = max(max_sum, fix_size_sum)
        return max_sum/k