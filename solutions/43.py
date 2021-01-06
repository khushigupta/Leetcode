class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        if num1 == "1":
            return num2

        if num2 == "1":
            return num1

        num1 = list(num1)
        num2 = list(num2)

        num1.reverse()
        num2.reverse()

        """
        if it's 123 X 456
          456 (num2)
        x 123 (num1)
        -------
        """

        final_sum = ""
        carry = 0

        for i, n1 in enumerate(num1):
            curr_sum = ""

            for k in range(i):
                curr_sum += "0"

            for j, n2 in enumerate(num2):
                prod = (int(n1) * int(n2)) + carry
                q, r = int(prod / 10), prod % 10
                curr_sum += str(r)
                carry = q
            if carry != 0:
                curr_sum += str(carry)
                carry = 0

            final_sum = self.add(curr_sum, final_sum)

        return final_sum[::-1]

    def add(self, curr_sum, final_sum):
        if final_sum == "":
            return curr_sum

        return_sum = ""

        C = len(curr_sum)
        F = len(final_sum)

        carry = 0
        for i in range(C):
            if i < F:
                inter = int(curr_sum[i]) + int(final_sum[i]) + carry
                q, r = int(inter / 10), inter % 10
                return_sum += str(r)
                carry = q
            else:
                inter = int(curr_sum[i]) + carry
                q, r = int(inter / 10), inter % 10
                return_sum += str(r)
                carry = q

        if F == C:
            if carry != 0:
                return_sum += str(carry)
            return return_sum

        if i < F:
            while i < F:
                inter = int(final_sum[i]) + carry
                q, r = int(inter / 10), inter % 10
                return_sum += str(r)
                carry = q
                i += 1

        if carry != 0:
            return_sum += str(carry)

        return return_sum

