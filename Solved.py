# -*- coding: utf-8 -*-

#Created on Tue Sep  1 11:10:25 2020

#author: stuart

from typing import List
from random import randint



# 728. Self Dividing Numbers
# A self=dividing num is one that is divisible by every digit it contains
# not allowed to contain the digit zero
# lower and upper number bound, output list of every possible self div num
# including the bounds

# conversion to string

# second solution is not my own but avoids converting to string so faster
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # make a range right - left for which to run through 
        # then make a list of those numbers starting from left 
        # Actually for i in range (abs(lef-right))
            # list.append value[i] + 1

        ans = []
        temp = []
        rang = abs(right - left)
        
        for i in range(rang):
            temp.append(left + i)
        temp.append(right)
        
        
        for i in range(len(temp)):
            number = temp[i]
            number = str(number)
            #print("length",len(number))
            count = 0 
            for i in range(len(number)):
                number2 = int(number)
                digit = int(number[i])
                print("number", number2)
                if digit != 0 and number2 % digit == 0: 
                    count += 0 
                else:
                    count += 1
            print("count", count)
            if count == 0:
                ans.append(int(number))
                
                
        
        
        return ans
        
    


    
    
ans = Solution()
print(ans.selfDividingNumbers((1),(22)))

# ans [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]



"""
# 1299. Replace Elements with Greatest Element on Right Side
# last one gets replaced with -1

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       #arr[i] = max list to the right 
        # my answer further below is correct but too slow
        # the trick to reduce on looping is to do in reverse
        
    
        rightMax = -1
        # reverse iteration
        # 1st -1 means start at end
        # second means reverse order
        #third means stop at first
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
            return arr
        
        
        # second option
        i = len(arr) - 1
        mx = arr[i]
        arr[i] = -1
        
        while i > 0:
            i -= 1
            arr[i], mx = mx, max(mx, arr[i])
        
        return arr
        
        
        
        ans = []
        l = len(arr)
        temp = 0
        for i in range(l-1):
            #print(arr[i + 1])
            temp = 0
            while i < l-1:
                if arr[i + 1] >= temp:
                    temp = arr[i + 1]
                    i += 1
                else:
                    i +=1
            ans.append(temp)
        ans.append(-1)
        return ans
                  
        

ans = Solution()
print(ans.replaceElements([5,11,4,3,5,1,0,5,0]))
# ans should be  = [18,6,6,6,1,-1]
"""


"""
# COME BACK MAKE UNIQUE
# 1304. Find N Unique Integers Sum up to Zero

#Given an integer n, return any array containing n unique integers
# such that they add up to 0.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n-1):
            ans.append(randint(-100,100))
        
        unique_list = []
        for i in ans:
            if i not in unique_list:
                unique_list.append(i)
        lost = len(ans) - len(unique_list)
        print(lost)
        
        
        d = {}
        for i in ans:
            if i not in d:
                d[i]=1
            else:
                d[i] += 1
                
        final = []
        multi = 0
        for key, value in d.items():
            while value != 1:
                multi = key
            final.append(key)
                
            
        
        final = []
        for key, value in d.items():
            if value == 1:
                final.append(key)
            else:
                key =+ 1
                
                
            
            
            
            
        addition = sum(ans)
        addition = addition * -1
        ans.append(addition)       
        
        return ans

ans = Solution()
print(ans.sumZero(100))
"""



"""
# 1436. Destination City

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # this is wayyy too long
        
        # could do a dict

        # could do pairs of the second values
        destinations = []
        starting = []
        total = []
        for i in range(len(paths)):
            destinations.append(paths[i][1])
            starting.append(paths[i][0])
            
        total = destinations + starting
        
        d = {}
        for i in total:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        final = []  
        for key, value in d.items():
            if value == 1:
                final.append(key)
        
        merged = final + destinations
        
        d2 = {}
        for i in merged:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
                
        for key, value in d.items():
            if value == 1:
                return key
        
            
ans = Solution()
print(ans.destCity([["London","New York"],["Lima","Sao Paulo"],["New York","Lima"]]))
"""



"""
# 1266. Minimum Time Visiting All Points
# have to vist all points in order from lowest to highest 
# +1 vert +1 hor or +1 vert 
# abs function prints absolute value
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #print(points)
        #print(points[0])
        # print(points[0][0]) # first speaks to the coordinates pair second speaks to x or y
        
        
        l=len(points)
        ans=0
        for i in range(l-1):
            x=abs(points[i][0]-points[i+1][0])
            y=abs(points[i][1]-points[i+1][1])
            ans+=max(x,y)
        return ans
        
    
ans=Solution()
print(ans.minTimeToVisitAllPoints([[3,2],[8,4],[5,1]]))
 """       

"""
# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        count = 0
        current = 0
        for i in range(l):
            current = nums[i]
            for i in range(l):
                if current > nums[i]:
                    count += 1
            ans.append(count)
            count = 0
        return ans

            
        
ans = Solution()
print(ans.smallerNumbersThanCurrent([6,5,4,8]))
"""
    
        
        



"""
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
            while number >= 1:
                number = number / 10
                count = count + 1
            ans.append(count)
            count = 0
        print(ans)
    
        ans2 = 0
        i = 0
        l = len(ans)
        while i < l:
            if ans[i] % 2 == 0:
                #ans2 + 1
                ans2 += 1
                i += 1
            else:
                i += 1
        return ans2
   
    
ans = Solution()
print(ans.findNumbers([100000]))
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