class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        N = len(piles)
        if H <= N:
            return max(piles)

        return self.find_k(piles, H)

    def find_k(self, piles, H):
        high = max(piles)
        low = 1

        eating_speed = high
        while low <= high:
            k = (high + low) // 2
            num_hours = self.num_hours(piles, k)
            if num_hours == H:
                # this may not be the minimum!
                eating_speed = min(eating_speed, k)
                break
            if num_hours > H:
                low = k - 1
            if num_hours < H:
                high = k + 1

        # while True:
        #     num_hours = self.num_hours(piles, eating_speed - 1)
        #     if num_hours == H:
        #         eating_speed = eating_speed - 1
        #     else:
        #         break
        # return eating_speed

    def num_hours(self, piles, k):
        total_hours = 0
        for p in piles:
            q = int(p / k)
            total_hours += q
            if p - q * k != 0:
                total_hours += 1
        return total_hours
