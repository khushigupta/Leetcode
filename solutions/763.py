from collections import defaultdict


class Solution(object):
    def takeFirst(self, elem):
        return elem[0]

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        ind = defaultdict(list)
        S = list(S)

        for i, s in enumerate(S):
            if s in ind:
                ind[s] = [min(i, ind[s][0]), max(i, ind[s][1])]
            else:
                ind[s] = [i, i]

        indices = [v for _, v in ind.items()]
        indices = sorted(indices, key=self.takeFirst)
        print(indices)
        result = []

        min_idx = indices[0][0]
        max_idx = indices[0][1]
        for i in range(1, len(indices)):
            if indices[i][0] < max_idx:
                min_idx = min(min_idx, indices[i][0])
                max_idx = max(max_idx, indices[i][1])
            else:
                result.append(max_idx - min_idx + 1)
                min_idx = indices[i][0]
                max_idx = indices[i][1]

        result.append(max_idx - min_idx + 1)
        return result