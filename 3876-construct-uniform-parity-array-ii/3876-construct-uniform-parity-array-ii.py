class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for x in nums1:
            if x % 2 == 0:
                minEven = min(minEven, x)
            else:
                minOdd = min(minOdd, x)

        if minOdd == float('inf'):
            return True
        if minEven == float('inf'):
            return True
        return minOdd < minEven