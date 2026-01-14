class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object): # converting the linkedlist into list
    def isPalindrome(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        if nums == nums[::-1]:
            return True
        else:
            return False
        
        # if you dont want to use sclicing

        # l,r = 0 , len(nums) -1
        # while l<=r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l +=1
        #     r -=1
        # return True
