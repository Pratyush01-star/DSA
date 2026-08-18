class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        count = [0] * 51

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] += 1

        for x in range(50, -1, -1):
            if count[x] == 1:
                return x

        return -1