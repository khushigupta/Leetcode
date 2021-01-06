class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        M = len(board)
        if M == 0:
            return board

        N = len(board[0])

        for i in range(M):
            for j in range(N):
                self.get_new_state(i, j, M, N, board)
        for i in range(M):
            for j in range(N):
                board[i][j] = board[i][j] // 4
        return

    def is_valid(self, row, col, M, N):
        if 0 <= row < M and 0 <= col < N:
            return True
        return False

    def get_new_state(self, row, col, M, N, board):
        char = board[row][col] % 2
        n_x = [-1, 0, 1]
        n_y = [-1, 0, 1]

        num_live = 0
        for x in n_x:
            for y in n_y:
                if x == 0 and y == 0:
                    continue
                row_idx = row + x
                col_idx = col + y
                if not self.is_valid(row_idx, col_idx, M, N):
                    continue
                if board[row_idx][col_idx] % 2 == 1:
                    num_live += 1

        # if live:
        if char == 1:
            if num_live == 2 or num_live == 3:
                new_val = 5
            else:
                new_val = 3
        else:  # if dead
            if num_live == 3:
                new_val = 4
            else:
                new_val = 2
        board[row][col] = new_val



