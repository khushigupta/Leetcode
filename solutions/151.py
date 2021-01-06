# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s = list(s)
#         ptr1 = 0
#         ptr2 = 0
#         end = len(s)
#         while ptr2 < end:
#             while ptr2 < end and s[ptr2] != " ":
#                 ptr2 += 1
#             self.reverse_word(s, ptr1, ptr2-1)
#             while ptr2 < end and s[ptr2] == " ":
#                 ptr2 += 1
#             ptr1 = ptr2
#         self.reverse_word(s, 0, end - 1)
#         ans = self.remove_space(s)
#
#         if len(ans) == 0:
#             return ""
#         return "".join(ans)
#
#     def remove_space(self, s):
#         idx = 0
#         # leading 0s
#         while idx < len(s) and s[idx] == " ":
#             idx += 1
#         start = idx
#
#         idx = len(s) - 1
#         while idx >= 0 and s[idx] == " ":
#             idx -= 1
#         end = idx
#         if start > end:
#             return []
#
#         # remove spaces in between
#         ptr1 = start
#         ptr2 = ptr1
#         length = 0
#
#         while ptr1 <= end:
#             while ptr1 <= end and s[ptr1] != " ":
#                 s[ptr2] = s[ptr1]
#                 ptr2 += 1
#                 ptr1 += 1
#                 length += 1
#             if ptr2 <= end:
#                 s[ptr2] = " "
#                 ptr2 += 1
#                 length += 1
#             while ptr1 <= end and s[ptr1] == " ":
#                 ptr1 += 1
#
#         return s[start:start+length+1]
#
#     def reverse_word(self, s, start, end):
#         ptr1 = start
#         ptr2 = end
#         while ptr1 < ptr2:
#             s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
#             ptr1 += 1
#             ptr2 -= 1


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        self.remove_space(s)
        i = 0
        for j in range(len(s)):
            if s[j] == " ":
                continue
            if s[j] == "*":
                self.reverse_word(s, i, j-1)
                i = j+1
        print(s, i, j)
        self.reverse_word(s, 0, len(s) - 1)
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return ""

        if s[i] == "*":
            i += 1
        if s[-1] == "*":
            s = s[i:-1]
        else:
            s = s[i:]
        for j in range(len(s)):
            if s[j] == "*":
                s[j] = " "

        return "".join(s)
    def remove_space(self, s):
        for i in range(1, len(s)):
            if s[i] == " " and s[i-1] != " " and s[i-1] != "*":
                s[i] = "*"
        i = 0
        j = 0

        while j < len(s):
            if s[j] != " ":
                s[i], s[j] = s[j], s[i]
                i += 1
                j += 1
            else:
                j += 1

    def reverse_word(self, s, start, end):
        ptr1 = start
        ptr2 = end
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1

s = Solution()
a = 'the sky is blue'
ans = s.reverseWords(a)
print(ans)