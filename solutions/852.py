class Solution(object):
    A = None

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return 0

        if len(A) == 2:
            return 0 if A[0] > A[1] else 1

        self.A = A
        return self.find(0, len(A) - 1)

    def find(self, low, high):

        while low <= high:

            mid = (low + high) // 2
            next = mid + 1
            prev = mid - 1

            if prev == -1:
                return mid if self.A[mid] > self.A[next] else next
            if next == len(self.A):
                return mid if self.A[mid] > self.A[prev] else prev

            if next < len(self.A) and self.A[mid] > self.A[next] and prev > -1 and self.A[mid] > self.A[prev]:
                return mid

            if next < len(self.A) and self.A[mid] > self.A[next] and prev > -1 and self.A[mid] < self.A[prev]:
                high = prev

            if next < len(self.A) and self.A[mid] < self.A[next] and prev > -1 and self.A[mid] > self.A[prev]:
                low = next