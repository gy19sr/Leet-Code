# -*- coding: utf-8 -*-

#Created on Tue Sep  1 11:10:25 2020

#author: stuart



# 136. Single Number

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
      #  j = 0
        leng = len(nums)
    #    while j < leng:
        for i in range(leng):
            if nums[i] == nums[0]:
                print('pair')
            else:
                print('not pair')
        #    j += 1
        return answer

ans = Solution()
print(ans.singleNumber([2,2,3,3,5]))


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
            #k = num_of_kids[i]
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