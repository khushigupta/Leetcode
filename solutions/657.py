class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves = list(moves)
        move_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

        start = (0, 0)
        pos = start
        for m in moves:
            pos = (pos[0] + move_dict[m][0], pos[1] + move_dict[m][1])

        if pos[0] == 0 and pos[1] == 0:
            return True
        return False