class Solution(object):
    def removeElement(self, nums, val):
        startIndex = 0
        searchedNums = 0
        while searchedNums < len(nums):
            checkNum = nums[startIndex]
            searchedNums += 1
            if checkNum == val:
                for i in range(startIndex + 1, len(nums)):
                    nums[i - 1] = nums[i]
                nums[-1] = checkNum
            else:
                startIndex += 1
        return startIndex


print(Solution().removeElement([3, 2, 2, 3], 3))
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
