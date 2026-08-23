class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Difference in number of '?'
        q_diff = left_q - right_q

        # Difference in known digit sums
        sum_diff = left_sum - right_sum

        # If '?' counts are equal, Bob can always mirror Alice.
        if q_diff == 0:
            return sum_diff != 0

        # Alice can force an unequal sum when the imbalance
        # cannot be exactly compensated.
        return sum_diff * 2 != -9 * q_diff