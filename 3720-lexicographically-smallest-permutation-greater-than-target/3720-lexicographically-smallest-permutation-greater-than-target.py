class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        chars = sorted(s)
        n = len(s)
        for i in range(n - 1, -1, -1):
            prefix = target[:i]

            remaining = chars.copy()
            possible = True

            for ch in prefix:
                if ch in remaining:
                    remaining.remove(ch)
                else:
                    possible = False
                    break

            if not possible:
                continue
            greater = [ch for ch in remaining if ch > target[i]]

            if greater:
                c = min(greater)
                remaining.remove(c)

                return prefix + c + ''.join(remaining)

        return ""