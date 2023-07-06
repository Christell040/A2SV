class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        x = len(arr)
        k = []
        for i in range(x):
            maximum = max(arr[:x-i])
            max_index = arr.index(maximum)+1
            arr[:max_index] = reversed(arr[:max_index])
            k.append(max_index)

            arr[:x-i] = reversed(arr[:x-i])
            k.append(x-i)
        return k