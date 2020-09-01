# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:10:25 2020

@author: stuart
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