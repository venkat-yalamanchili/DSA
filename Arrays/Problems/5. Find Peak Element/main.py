def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            # Ascending slope: peak must be to the right
            l = mid + 1
        else:
            # Descending slope: peak is to the left or at mid
            r = mid
    return l  # or r, since l == r