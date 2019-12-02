"""""Given an array nums of n integers, are there elements a, b, c in nums such
#  that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#Note:
#The solution set must not contain duplicate triplets.
#Example:
#Given array nums = [-1, 0, 1, 2, -1, -4],

#A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
] """

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """        
    # if less than three numbers, don't bother searching
    if len(nums) < 3:
        return []

    # sort nums and use current sum to see if should have larger number or smaller number
    nums = sorted(nums)
    triplets = []
    
    for i in range(len(nums)-2):    # i point to first number to sum in list
        j = i + 1                   # j points to middle number to sum in list
        k = len(nums) - 1           # k points to last number to sum in list
        while j < k:
            currSum = nums[i] + nums[j] + nums[k]
            if currSum == 0:
                tmpList = sorted([nums[i], nums[j], nums[k]])
                if tmpList not in triplets:
                    triplets.append(tmpList)
                j += 1 # go to next number to avoid infinite loop
            # sum too large, so move k to smaller number
            elif currSum > 0:
                k -= 1
            # sum too small so move j to larger number
            elif currSum < 0:
                j += 1
    return triplets

        

    



 
  
nums = [-1, 0, 1, 2, -1, -4]

print(threeSum(nums))