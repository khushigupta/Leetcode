from collections import defaultdict, Counter
import heapq as heap


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums

        cnt_dict = Counter(nums)
        val_dict = defaultdict(list)
        for key, cnt in cnt_dict.items():
            val_dict[cnt].append(key)
        cnt_list = cnt_dict.values()

        # max heap
        H = cnt_list[:k]
        heap.heapify(H)
        for c in cnt_list[k:]:
            min_val = heap.heappop(H)
            if c > min_val:
                heap.heappush(H, c)
            else:
                heap.heappush(H, min_val)

        heap_size = k
        ans = []
        while heap_size:
            cnt = heap.heappop(H)
            ans.append(val_dict[cnt].pop())
            heap_size -= 1
        return ans

