from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                L = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // L

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left