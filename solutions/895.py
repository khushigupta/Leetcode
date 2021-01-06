from collections import defaultdict
import heapq as heap


class FreqStack(object):

    def __init__(self):
        self.freq_dict = defaultdict(int)
        self.H = []
        heap.heapify(self.H)
        self.stack_idx = None
        self.stack = []
        self.second_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack_idx = 1
        else:
            self.stack_idx = self.stack[-1][1] + 1
        self.stack.append((x, self.stack_idx))
        self.freq_dict[x] += 1
        heap.heappush(self.H, (-self.freq_dict[x], -self.stack_idx, x))

    def pop(self):
        """
        :rtype: int
        """
        freq, idx, num = heap.heappop(self.H)
        top = self.stack.pop()
        while top[0] != num:
            self.second_stack.append(top)
            top = self.stack.pop()

        while len(self.second_stack):
            push = self.second_stack.pop()
            self.stack.append(push)

        self.freq_dict[num] -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()