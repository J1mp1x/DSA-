class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)

        nums.sort(key=lambda x: (freq[x], -x))
        return nums