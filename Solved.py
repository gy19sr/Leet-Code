# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:10:25 2020

@author: stuart
"""


# 1431. Kids With the Greatest Number of Candies
#
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num_of_kids = candies
        i = 0 # the number of kids 
        while i < len(num_of_kids):
            print("test")
            i += 1
  """          
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int]) -> int:
        num_of_kids = candies
        i = 0 # the number of kids 
        while i < len(num_of_kids):
            print("test")
            i += 1
        if i == len(num_of_kids):
            return 
            
ans = Solution()
print(ans.kidsWithCandies([14, 11, 22]))
            












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