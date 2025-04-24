class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        rank = {value: index for index, value in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (rank.get(x, len(arr2) + x)))