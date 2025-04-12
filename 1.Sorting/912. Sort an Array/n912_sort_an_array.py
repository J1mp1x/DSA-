class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # If left child exists and is greater than root
            if left < n and arr[left] > arr[largest]:
                largest = left

            # If right child exists and is greater than largest so far
            if right < n and arr[right] > arr[largest]:
                largest = right

            # If largest is not root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                heapify(arr, n, largest)

        n = len(nums)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # swap
            heapify(nums, i, 0)

        return nums