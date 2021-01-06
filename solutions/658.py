class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # find insertion index of x, then have two pointers that go in either direction, adding elements to the left or right

        idx = self.find_insertion_index(arr, x)

        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[-k:]

        final_arr = []
        if arr[idx] == x:
            low = idx - 1
            high = idx + 1
            final_arr.append(arr[idx])
            k = k - 1
        else:
            low = idx
            high = idx + 1

        count = 0
        while count < k:
            if low >= 0 and high < len(arr):
                if abs(arr[low] - x) <= abs(arr[high] - x):
                    final_arr.append(arr[low])
                    low -= 1
                else:
                    final_arr.append(arr[high])
                    high += 1
            elif low >= 0:
                final_arr.append(arr[low])
                low -= 1
            else:
                final_arr.append(arr[high])
                high += 1
            count += 1

        final_arr.sort()
        return final_arr

    def find_insertion_index(self, arr, x):
        if x <= arr[0]:
            return 0
        if x >= arr[-1]:
            return len(arr)

        low = 0
        high = len(arr) - 1
        idx = -1

        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                idx = mid
                break
            if arr[mid] > x:
                high = mid - 1
            if arr[mid] < x:
                low = mid + 1

        if idx == -1:
            idx = mid
        return idx


