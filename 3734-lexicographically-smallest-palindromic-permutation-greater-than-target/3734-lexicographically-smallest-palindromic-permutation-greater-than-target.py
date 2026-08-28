class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = [i for i in range(26) if cnt[i] % 2]

        if len(odd) > 1:
            return ""

        m = n // 2

        half = [x // 2 for x in cnt]

        middle = ""
        if n % 2:
            middle = chr(97 + odd[0])

        def make_pal(h):
            if n % 2 == 0:
                return h + h[::-1]
            return h + middle + h[::-1]

        t = target[:m]
        rem = half[:]
        equal_possible = True

        for ch in t:
            x = ord(ch) - 97
            if rem[x] == 0:
                equal_possible = False
                break
            rem[x] -= 1

        if equal_possible:
            candidate = make_pal(t)

            if candidate > target:
                return candidate

        for i in range(m - 1, -1, -1):

            rem = half[:]
            possible = True

            for j in range(i):
                x = ord(t[j]) - 97

                if rem[x] == 0:
                    possible = False
                    break

                rem[x] -= 1

            if not possible:
                continue

            current = ord(t[i]) - 97

            for c in range(current + 1, 26):

                if rem[c] == 0:
                    continue

                rem[c] -= 1

                suffix = []

                for x in range(26):
                    if rem[x] > 0:
                        suffix.append(chr(97 + x) * rem[x])

                h = t[:i] + chr(97 + c) + ''.join(suffix)

                return make_pal(h)

        return ""