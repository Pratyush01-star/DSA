class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        left = 0

        while left < n:
            right = left

            while right + 1 < n and arr[right + 1][0] - arr[right][0] <= limit:
                right += 1

            values = [arr[i][0] for i in range(left, right + 1)]

            indices = sorted(arr[i][1] for i in range(left, right + 1))
            for idx, value in zip(indices, values):
                ans[idx] = value

            left = right + 1

        return ans