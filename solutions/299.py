from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = [int(s) for s in secret]
        guess = [int(g) for g in guess]

        s_dict = defaultdict(list)
        g_dict = defaultdict(list)

        for i, num in enumerate(secret):
            s_dict[num].append(i)

        for i, num in enumerate(guess):
            g_dict[num].append(i)

        num_cows = 0
        num_bulls = 0

        for key, value in s_dict.items():
            if key not in g_dict:
                continue
            num_cows += min(len(value), len(g_dict[key]))

        for i, num in enumerate(secret):
            if i < len(guess):
                if secret[i] == guess[i]:
                    num_bulls += 1

        num_cows = num_cows - num_bulls

        return "{}A{}B".format(num_bulls, num_cows)

