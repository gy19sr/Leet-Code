# -*- coding: utf-8 -*-

#Created on Tue Sep  1 11:10:25 2020

#author: stuart

from typing import List

# 1295. Find Numbers with Even Number of Digits

# fun practice find how many even numbers
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] % 2 == 0:
                ans + 1
                ans += 1
                i += 1
            else:
                i += 1
        return ans
        
ans = Solution()
print(ans.findNumbers([12,345,2,6,7896]))



# now actual solution

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        i = 0
        l = len(nums)
        ans = []
        number = 0
        
        for i in range(l):
            number = nums[i]
            while number > 1:
                number = number / 10
                count = count + 1
            ans.append(count)
            count = 0
        
        print(ans)
    
    
    
    
    
    
ans = Solution()
print(ans.findNumbers([12,345,2,6,7896]))

"""
# COME BACK TO IT
# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        l = len(nums)
        y = 0 
        while i < l:
            if nums[i] >= list next value:
                ans.append(1)
            i += 1
            
        
ans = Solution()
print(ans.smallerNumbersThanCurrent([8,2,4,3,1]))
"""



"""
# 217. Contains Duplicate
# find if array has any duplicates

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for number in nums:
            if number not in d:
                d[number] = 1
            else:
                d[number] += 1
           
        list2 = []
        for key, value in d.items():
            if value >= 2:
                list2.append(True)
            else:
                list2.append(False)
        
        i = 0 
        ans = True
        ans2 = False
        while i < len(list2):
            if list2[i] == True:
                return(ans)
            else:
                i += 1
        return(ans2)
            
        
ans = Solution()
print(ans.containsDuplicate([2,14,6,11,0,1,5,19,13]))
"""

"""
#283. Move Zeroes
# using append() + pop() + index()
# move zeros to the back of the list
# look at difference between .pop() and .remove()

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # Do not return anything, modify nums in-place instead.
        
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                
                i += 1
            else:
                i += 1
        return nums
        
        #i = 0 
        #if i < l and nums[i] == 0:
         #   nums.append(0)
          #  nums.pop(0)
           # i += 1
        #else:
         #   i += 1
        #return nums
        
ans = Solution()
print(ans.moveZeroes([0,0,1]))
"""


"""
# 136. Single Number
# find the one that doesn't have a pair

# solution 1
# dict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for number in nums:
            if number not in d:
                d[number] = 1
            else:
                d[number] += 1
                
        for key, value in d.items():
            if value == 1:
                return key 
        
ans = Solution()
print(ans.singleNumber([2,5,3,3,2]))

# solution 2
# sets, sets are unique items
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
        
        
ans = Solution()
print(ans.singleNumber([1,1,2,2,3]))


# solution 3
# duplicates

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
                for i in nums:
                    if i not in no_duplicate_list:
                        no_duplicate_list.append(i)
                    else:
                        no_duplicate_list.remove(i)
                return no_duplicate_list.pop()
ans = Solution()
print(ans.singleNumber([1,1,2,2,3]))
"""


"""
# 1480. Running Sum of 1d Array


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        total_addition = 0
        leng = len(nums)
        answer = []
        while i < leng:     
            answer.append(nums[i] + total_addition)
            total_addition = total_addition + nums[i]
            i += 1
        return answer

ans = Solution()
print(ans.runningSum([1,2,3,4]))
"""         
        



"""
# 1431. Kids With the Greatest Number of Candies
# print bool list of whether kids can have the most in the list
 


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=len(candies)
        ans=[]
        y=0
        i=0
        while i < l: 
            if y <= candies[i]:
                y = candies[i]
            i += 1
        
        for i in range(l): # seems same as while i < 1 method
            if candies[i]+extraCandies >= y:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    
answer = Solution()
print(answer.kidsWithCandies([14,4,8],7))
"""




"""
1342. Number of Steps to Reduce a Number to Zero


class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0 # initial number of steps
        number = num # number of input value    
        while number != 0: 
            if number % 2==0:
                
               steps += 1
               number = number/2 
            else:
                steps += 1
                number -= 1
        return steps
ans = Solution()
print(ans.numberOfSteps(14))
    
"""