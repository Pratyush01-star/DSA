class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        s=set()
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j and a[i] != 0:
                    for k in range(len(a)):
                        if i !=k and j !=k and a[k] % 2 == 0:
                            s.add(a[i] * 100 + a[j] * 10 + a[k])
        return len(s)
