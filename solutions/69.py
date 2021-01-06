class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        if x < 3:
            return 1

        low = 1
        high = x // 2

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1

        if mid * mid > x:
            return mid - 1
        return mid


