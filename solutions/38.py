class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        curr_str = '1'
        for i in range(1, n):
            curr_str = self.create_string(curr_str)
        return curr_str

    def create_string(self, num_str):
        num_arr = [int(n) for n in num_str]
        return_arr = []
        count = 1
        i = 0

        for i in range(1, len(num_arr)):
            if num_arr[i] == num_arr[i - 1]:
                count += 1
            else:
                return_arr += [count, num_arr[i - 1]]
                count = 1
        return_arr += [count, num_arr[i]]

        return_arr = [str(r) for r in return_arr]
        return ''.join(return_arr)

