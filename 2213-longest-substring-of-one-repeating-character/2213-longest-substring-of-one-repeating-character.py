class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)
        arr = list(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            left_char = a[0]
            right_char = b[1]

            length = a[5] + b[5]

            prefix = a[2]
            if a[2] == a[5] and a[1] == b[0]:
                prefix = a[5] + b[2]

            suffix = b[3]
            if b[3] == b[5] and a[1] == b[0]:
                suffix = b[5] + a[3]

            best = max(a[4], b[4])

            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        def build(node, left, right):
            if left == right:
                c = arr[left]
                tree[node] = [c, c, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index):
            if left == right:
                c = arr[index]
                tree[node] = [c, c, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index)
            else:
                update(node * 2 + 1, mid + 1, right, index)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        build(1, 0, n - 1)
        answer = []
        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            char = queryCharacters[i]

            arr[index] = char

            update(1, 0, n - 1, index)
            answer.append(tree[1][4])

        return answer