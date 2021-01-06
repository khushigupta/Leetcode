class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n < 3:
            return 1

        low = 1
        high = n

        while low <= high:
            k = (low + high) // 2
            coins_used = (k * (k + 1)) // 2
            if coins_used == n:
                return k
            if coins_used > n:
                high = k - 1
            if coins_used < n:
                low = k + 1

        if (k * (k + 1)) // 2 < n:
            return k
        else:
            return k - 1
