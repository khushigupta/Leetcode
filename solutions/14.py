class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        i = 0
        while True:
            first_str = strs[0]
            found = True
            if i == len(first_str):
                return first_str

            for j in range(1, len(strs)):
                next_str = strs[j]
                if i == len(next_str):
                    return next_str
                if next_str[i] != first_str[i]:
                    found = False
                    break
                first_str = next_str
            if not found:
                break
            i += 1

        return first_str[:i]
