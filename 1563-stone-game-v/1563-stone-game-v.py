class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # leftBest[l][r] =
        # max(sum(l..k) + dp[l][k]) for k in [l, r]
        leftBest = [[0] * n for _ in range(n)]

        # rightBest[l][r] =
        # max(sum(k..r) + dp[k][r]) for k in [l, r]
        rightBest = [[0] * n for _ in range(n)]

        for i in range(n):
            leftBest[i][i] = stoneValue[i]
            rightBest[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # Binary search first k where:
                # left >= right
                lo, hi = l, r - 1

                while lo < hi:
                    mid = (lo + hi) // 2

                    left = prefix[mid + 1] - prefix[l]

                    if left * 2 >= total:
                        hi = mid
                    else:
                        lo = mid + 1

                k = lo

                left = prefix[k + 1] - prefix[l]
                right = total - left

                if left == right:
                    dp[l][r] = left + max(
                        dp[l][k],
                        dp[k + 1][r]
                    )

                elif left > right:
                    # For all splits before k:
                    # left < right
                    #
                    # At k:
                    # left > right
                    dp[l][r] = rightBest[k + 1][r]

                    if k > l:
                        dp[l][r] = max(
                            dp[l][r],
                            leftBest[l][k - 1]
                        )

                else:
                    # This happens only when k == r-1
                    dp[l][r] = leftBest[l][k]

                # Build leftBest[l][r]
                leftBest[l][r] = max(
                    leftBest[l][r - 1],
                    (prefix[r + 1] - prefix[l]) + dp[l][r]
                )

                # Build rightBest[l][r]
                rightBest[l][r] = max(
                    rightBest[l + 1][r],
                    (prefix[r + 1] - prefix[l]) + dp[l][r]
                )

        return dp[0][n - 1]