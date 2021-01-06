from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s

        char_to_cnt_dict = defaultdict(int)
        for c in s:
            char_to_cnt_dict[c] += 1

        cnt_to_char_dict = defaultdict(list)
        for key, val in char_to_cnt_dict.items():
            cnt_to_char_dict[val].append(key)

        sorted_values = sorted(cnt_to_char_dict.keys(), reverse=True)

        ans = []
        for v in sorted_values:
            char_list = cnt_to_char_dict[v]
            for c in char_list:
                ans += [c] * v
        return ''.join(ans)