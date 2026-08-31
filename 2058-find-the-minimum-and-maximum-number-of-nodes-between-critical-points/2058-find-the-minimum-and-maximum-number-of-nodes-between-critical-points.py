class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            isMax = curr.val > prev.val and curr.val > curr.next.val
            isMin = curr.val < prev.val and curr.val < curr.next.val

            if isMax or isMin:
                if first == -1:
                    first = index
                else:
                    minDist = min(minDist, index - last)

                last = index
            prev = curr
            curr = curr.next
            index += 1
        if first == last:
            return [-1, -1]
        maxDist = last - first
        return [minDist, maxDist]