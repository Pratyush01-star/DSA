class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIdx = nums.index(min(nums))
        maxIdx = nums.index(max(nums))

        left = min(minIdx, maxIdx)
        right = max(minIdx, maxIdx)
        front = right + 1

        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)