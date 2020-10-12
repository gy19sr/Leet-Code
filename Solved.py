# -*- coding: utf-8 -*-

# Created on Tue Sep  1 11:10:25 2020

# author: stuart

# *** means review

from typing import List
from random import randint

# 961. N-Repeated Element in Size 2N Array

# In a array A of size 2N, there are N+1 unique elements,
# and exactly one of these elements is repeated N times.

# Return the element repeated N times.

# dic is first idea for a solution

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        l = len(A)
        N =l/2
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key, value in d.items():
            if value == N:
                return key



ans = Solution()
print(ans.repeatedNTimes([2,1,2,5,3,2]))

# Exp:
# Input: [1,2,3,3]
# Output: 3

# Input: [5,1,5,2,5,3,5,4]
# Output: 5




"""
# 1534. Count Good Triplets

#Given an array of integers arr, and
#three integers a, b and c. You need to find the number of good triplets.
#A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c


# a[start:stop:step] # start through not past stop, by step
# can specify the increment: range(2, 30, 3)

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # if it's less than or = to A then continue to next loop level
        # if it's less than or = to B check c
        # if <= c ans +1

        l = len(arr)
        ans = 0

        for i in range(l):
            for k in range(i + 1, l):
                if abs(arr[i] - arr[k]) > c: continue
                ans += sum(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b
                              for j in range(i + 1, k))
        return ans


ans = Solution()
print(ans.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))



# exp input [3,0,1,1,9,7], a = 7, b = 2, c = 3
# output: 4
# explanation There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)]
"""



"""
# 1588. Sum of All Odd Length Subarrays
# given an array of positive int., calc the sum of all possible odd-length subarrays
# return the sum of all odd length sub arrays

# best ans, not brute force
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854184/JavaC%2B%2BPython-O(N)-Time-O(1)-Space


def sumOddLengthSubarrays(self, A):
    res, n = 0, len(A)
            for i, a in enumerate(A):
                res += ((i + 1) * (n - i) + 1) / 2 * a
            return res

def sumOddLengthSubarrays(self, A):
    return sum(((i + 1) * (len(A) - i) + 1) / 2 * a for i, a in enumerate(A))



class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # need to figure out how many odd length sub arrays there are
        # can just sum all values to start for subarray length one
        # a[start:stop:step]
        # loops range (2, 6)
        ans = 0

        # need to create loop that creates 1s, then 3s, then 5s, etc
        # maybe a while loop

        # okay I will create sub arrays increasing by two in length each time
        # and I will subtract the earliest and add latest as long as fits in array

        ans += sum(arr)
        # for practice let's just do it with 3 for sub array length

        # for magical num start from 1 and + 2 until length of array
        # need to consider if array length is 6 how that would work
        k = 1
        while k <= len(arr):
            for i in range(len(arr)):
                sub = arr[i:i+k]
                leng = len(sub)
                if leng % 2 == 1 and leng != 1 and leng == k:
                    print(sub) # I ACCIDENTLY LEFT THIS IN SO IT COUNTED AS WRONG!!
                    ans += sum(sub)
            k += 2

        return ans
ans = Solution()
print(ans.sumOddLengthSubarrays([1,4,2,5,3,5,8]))
# exp. input: [1,4,2,5,3]
# output = 58
"""

"""
# 1450. Number of Students Doing Homework at a Given Time
#Given two integer arrays startTime and endTime
# and given an integer queryTime.
# Return the number of students doing their homework at time queryTime


# best answer
#return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
# zip(), what it does is merge like below
# number_list = [1, 2, 3]
# str_list = ['one', 'two', 'three']
# {(1, 'one'), (2, 'two'), (3, 'three')}

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        time = queryTime
        leng = len(startTime)
        for i in range(leng):
            temp_list = list(range(startTime[i], endTime[i]))
            temp_list.append(endTime[i])
            for i in range(len(temp_list)):
                if time == temp_list[i]:
                    ans += 1

            print(temp_list)
        return ans

ans = Solution()
print(ans.busyStudent([4],[4],4))

# example input start [1,2,3], endtime = [3,2,7], queryTime =4
"""


"""
# 26. remove duplicates from sorted Array
# given a sorted array nums, remove dups in place so each only appears once
# returns new length

# remove() removes the first matching value/object. It does not do anything with the indexing.
# pop() removes at a specific index and returns it
# del() removes the item at a specific index.

# best solution
# nums[:] = sorted(set(nums))
# return len(nums)


# nums[:] means whole list
# set() gets the unique values for an entire list seems to automatically sort them
# sorted () makes sure they're in order


#nums = [1,2,4,5,3,3,2,2,2,2]
#nums[:] = sorted(set(nums))
#return len(nums)
#print(nums[:])

#print("end of testing")

class Solution():
    def removeDuplicates(self, nums: List[int]) -> int:
        # so i will create a dictionary where any values greater than one will be reduced to just one occurence
        d = {}
        for i in nums: # so with a dictionary need to use the actual list not range(leng)
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for key, value in d.items():
            if value > 1:
                temp = value - 1
                #print(temp)
                for i in range(temp):
                    nums.remove(key)

        return len(nums)

ans = Solution()
print(ans.removeDuplicates([1,1,2,1,1]))
# function return len(num) = 5


#exp nums = [1,1,2]
#expected output 2
"""

# put onto website above

"""
# 70 Climbing Stairs
# each time yo can climb 1 or 2 steps. in how many distinct ways 
# can you climb to the top?

# *** this is a classic question 
# recursive programming
# Dynamic Programming, bottem up

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp[1] = 1 #as there is only one way to climb 1 step
        dp = [1] * (n + 1) # as you know 1 step is equal to one
        # so next can thin about number of ways for two steps
        # you start loop at second position because we know 1 and 
        # you just add 1 to the n
        for i in range(2, n + 1):
            # so now we know for value n 
            # we've come from either one or two steps before the current value
            dp[i] = dp[i - 1] + dp[i -2] # so to get to i there were only the two ways listed here
            #adding them works to figure out dp[i]
        return dp[n]

       
        
        
ans = Solution()
print(ans.climbStairs(3))
        
# input example 3
# output 3 Because 1+1+1, 1+2, 2+1

"""


"""
# 53 Maximum Subarray
# find the contiguous subarray which has the largest sum and return its sum


# lessons learned -
# loops range (2, 6) = specify the starting value to not including 6. if nothing there starts at zero
# can specify the increment: range(2, 30, 3)

# used below is an ARRAY SLICE syntax


#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array
#a[start:stop:step] # start through not past stop, by step


#a[-1]    # last item in the array
#a[-2:]   # last two items in the array
#a[:-2]   # everything except the last two items


#a[::-1]    # all items in the array, reversed
#a[1::-1]   # the first two items, reversed
#a[:-3:-1]  # the last two items, reversed
#a[-3::-1]  # everything except the last two items, reversed

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
        
          
        

        # my ans timed out, but listed below
        leng = len(nums)
        # so nums[i] then run through second list to find max and update and find nums[i] best leng
        # I can make a list for each and select the maximum of each list and append to new list
        max_list=[]
        for i in range(leng):
            #print(current_max)
            current_max=0 
             # need to remove the first one which will be zero
            temp_list = []
            
            while i < leng:
                #print(nums[i])
                current_max += nums[i] 
                temp_list.append(current_max)
                i += 1 # try and start at the correct number
                
            temp_max = max(temp_list)
            max_list.append(temp_max)
        
        print(max_list)
        
       # if len(max_list) > 1:
           # max_list.pop(0)
            
        print(max_list)
                
        ans = max(max_list)
        return ans

        
        
ans = Solution()
print(ans.maxSubArray([-1]))

# test input [-2,1,-3,4,-1,2,1,-5,4]
#output = 6 because of 4,-1,2,1




"""



"""
# 1460. Make Two Arrays Equal by Reversing Sub-arrays
## *** COME BACK LATER


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        for i in arr:
            if i not in arr:
                return False
            
            
            
            
        d = {}
        for i in target:
            if i not in d:
                d[i] = 1
            else:
                d[i] =+1
    
        
        d2 = {}
        for i in target:
            if i not in d:
                d2[i] = 1
            else:
                d2[i] =+1
        
        for key, value in d.items():
            if key != d2[key]:
                return key 

        
        
        
ans = Solution()
print(ans.canBeEqual([1,2,3,4],[2,4,1,3]))




# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
# 3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.

"""

"""
# 1475. Final Prices With a Special Discount in a Shop
# prices[i] - price[j]
# j is the minimum index 
# if prices[i] >= price[j] and j > i

# so basically the earliest number after the i that is less than it
# at least I think


#if not possible append price

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #ans = []
        l = len(prices)
        i = 0 
        
        while i <= l -2:
            for j in range(i+1, l):
                if prices[i] >= prices[j] and j > i:
                    prices[i] = prices[i] - prices[j]
                    break
            i += 1
        return prices
        
        
        
ans = Solution()
print(ans.finalPrices([8,4,6,2,3]))
# ans = [4,2,4,2,3]

"""




"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid)
        p = 0 # the number of columns that have had a negative and have now been counted
        #grid[i][i] first speaks to wich row second to which number
        
        
        # begin with first row
        # while value is postive countinue to search for num < 0 
        # if num less than zero ans += # rows
        
        
        # for the loop set the limit to the ones that are above zero
        
        
        for i in range(l): # run through loop for number of rows
            # first know how many to add if find a negative value in a row
            rows = l-i
           # print(rows)
            for k in range(len(grid[i]) - p): # for the length of an individual row
                
                j = grid[i][k]
                #print("num value", j)
                if j < 0:
                    ans += rows
                    p += 1

            
        
        
        
        return ans
        
        
ans = Solution()
print(ans.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

# ans = 8
"""



"""

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
            number = str(number) # all about converting to string
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



        ## Second Soultion ##
        result = []
        for n in range(left, right + 1): #didn't know I could do a range between two integers
            num = n
            is_self_div = True
            
            while num: # interesting need to look at what just while num implies
                digit = num % 10
                if not digit or (n % digit) != 0:
                    is_self_div = False
                    break
                num = num // 10
            
            if is_self_div:
                result.append(n) # appending value based on boolen, very cool
        
        return result
  
    
ans = Solution()
print(ans.selfDividingNumbers((1),(22)))

# ans [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


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