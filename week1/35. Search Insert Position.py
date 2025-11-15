# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):   #Method definition
        for i in range(len(nums)):  #Loop to iterate through the array
            if target == nums[i]: #Check if the current element matches the target
                return i #Return the index if a match is found
            elif target < nums[i]: #Check if the target is less than the current element
                return i #Return the index where the target would be inserted
        return len(nums)    #Return the length of the array if the target is greater than all elements

             

        
        