# -*- coding: utf-8 -*-

#Created on Tue Sep  1 11:10:25 2020

#author: stuart

from typing import List


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




"""
# 1480. Running Sum of 1d Array
from typing import List

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
#
 

from typing import List

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