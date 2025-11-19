class Solution(object):
    def isAnagram(self, s, t):
        
        sorted_s = sorted(s)  # Sort the first string
        sorted_t = sorted(t)  # Sort the second string

        return sorted_s == sorted_t  # Compare the sorted strings