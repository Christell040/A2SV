def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            # Swap non-zero element with the element at the left pointer
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    # Fill the remaining part of the array with zeros
    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums
