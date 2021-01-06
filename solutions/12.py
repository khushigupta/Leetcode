class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0 and num >= 4000:
            return ""

        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        return_string = ""
        ints = [1000, 100, 10, 1]
        idx = 0

        while num:
            curr_int = ints[idx]
            quotient, remainder = int(num / curr_int), num % curr_int

            if quotient == 0 and remainder == num:
                idx += 1
                continue
            if quotient == 9:
                prev_int = ints[idx - 1]
                return_string += roman[curr_int] + roman[prev_int]
            elif quotient >= 5 and quotient < 9:
                next_int = 5 * curr_int
                return_string += roman[next_int] + (quotient - 5) * roman[curr_int]
            elif quotient == 4:
                prev_int = 5 * curr_int
                return_string += roman[curr_int] + roman[prev_int]
            elif quotient >= 1 and quotient <= 3:
                return_string += (quotient) * roman[curr_int]

            num = remainder
            idx += 1

        return return_string




