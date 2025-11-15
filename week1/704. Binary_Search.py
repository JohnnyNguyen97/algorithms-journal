

# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object): 
    def search(self, nums, target): #Method definition
        for i in range(len(nums)): #Loop to iterate through the array
            if target == nums[i]: #Check if the current element matches the target
                return i #Return the index if a match is found
        return -1  #Return -1 if the target is not found
                
                    

        