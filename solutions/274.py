class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) < 1:
            return 0

        citations = sorted(citations)
        N = len(citations)
        max_citations = 0
        for i in range(len(citations)):
            if citations[i] >= N - i:
                max_citations = max(max_citations, N - i)
        return max_citations