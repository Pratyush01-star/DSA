class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        best = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            if ones == k:
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]
                if best == "" or len(current) < len(best):
                    best = current
                elif len(current) == len(best) and current < best:
                    best = current
                left += 1
                ones -= 1
        return best