class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        
        # Start merging from the end of the merged array
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Pointer for the merged array
        
        # Merge nums1 and nums2 by comparing elements from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Copy any remaining elements from nums2 to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1