class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])
        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total_litter = len(litter)

        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1
        q = deque()

        sr, sc = start
        q.append((sr, sc, 0, energy, 0))
        best = [[{} for _ in range(n)] for _ in range(m)]
        best[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, mask, e, moves = q.popleft()

            if mask == full_mask:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                if classroom[nr][nc] == 'R':
                    new_energy = energy
                old_energy = best[nr][nc].get(new_mask, -1)

                if new_energy <= old_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1