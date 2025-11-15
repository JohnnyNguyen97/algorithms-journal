# Two Sums

class Solution(object): #Class definition

    def twoSum(self, nums, target): #Method definition
        for i in range(len(nums)): #Loop to iterate through the array
            for j in range(i + 1, len(nums)): #Loop to check for pairs
                if nums[i] + nums[j] == target: #Check if the sum matches the target
                    return  [i, j] #Return the indices if a match is found
        return [] #Return an empty list if no pairs found
