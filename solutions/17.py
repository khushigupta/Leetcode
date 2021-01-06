class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or digits == "":
            return []

        digits = [int(s) for s in digits]
        digit_to_string = dict()
        digit_to_string[1] = ''
        digit_to_string[2] = 'abc'
        digit_to_string[3] = 'def'

        digit_to_string[4] = 'ghi'
        digit_to_string[5] = 'jkl'
        digit_to_string[6] = 'mno'

        digit_to_string[7] = 'pqrs'
        digit_to_string[8] = 'tuv'
        digit_to_string[9] = 'wxyz'

        string_list = []

        for d in digits:
            letters = list(digit_to_string[d])

            if len(string_list) == 0:
                string_list = letters
                continue

            curr_length = len(string_list)
            i = 0

            while (i < curr_length):
                head = string_list.pop(0)
                for l in letters:
                    string_list.append(head + l)
                i += 1

        return string_list



