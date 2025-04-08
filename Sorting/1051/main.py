class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        count = 0
        for h1, h2 in zip(heights, expected):
            if h1 != h2:
                count += 1
        return count