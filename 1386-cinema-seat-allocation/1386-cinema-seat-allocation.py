class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))) == 0
            middle = (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))) == 0
            right = (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9))) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans