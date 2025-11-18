def max_product(arr):
    max_product = 0
    for i in range (len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product=arr[i] * arr[j]
    return max_product

print(max_product([2,6,9,3,4,50]))


# Solution for simillar problem from leetcode, here this is the function that we are trying to get maximum (nums[i]-1)*(nums[j]-1)

def maxProduct(self, nums):
    max = 0
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if (nums[i]-1)*(nums[j]-1) > max:
                max = (nums[i]-1)*(nums[j]-1)
    return max