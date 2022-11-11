"""

def a(i, ls=[]):
    ls.append(i)
    return ls

print(a(10))

print(a(12, []))

print(a(13))

def MissingNo(arr):
    n = len(arr)
    total = (n + 1)*(n + 2)/2
    arr_sum = sum(arr)
    return total - arr_sum

print(MissingNo([1,2,3,4,7,8,9,10]))
"""
# GCD of more than two (or array) numbers

# Function implements the Euclidean
# algorithm to find H.C.F. of two number
def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


# Driver Code
l = [3,5,7]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])





from math import gcd
def solve(nums):
   if len(nums) == 1:
      return nums[0]

   div = gcd(nums[0], nums[1])

   if len(nums) == 2:
      return div

   for i in range(1, len(nums) - 1):
      div = gcd(div, nums[i + 1])
      if div == 1:
         return div

   return div

nums = [3,5,7]
# print(solve(nums))

# Code contributed by Mohit Gupta_OMG


# Python3 program to find longest
# alternating subsequence in an array

# Function to return max of two numbers
def Max(a, b):
    if a > b:
        return a
    else:
        return b


# Function to return longest alternating
# subsequence length
def zzis(arr, n):
    """las[i][0] = Length of the longest
        alternating subsequence ending at
        index i and last element is greater
        than its previous element
    las[i][1] = Length of the longest
        alternating subsequence ending
        at index i and last element is
        smaller than its previous element"""
    las = [[0 for i in range(2)]
           for j in range(n)]

    # Initialize all values from 1
    for i in range(n):
        las[i][0], las[i][1] = 1, 1

    # Initialize result
    res = 1

    # Compute values in bottom up manner
    for i in range(1, n):

        # Consider all elements as
        # previous of arr[i]
        for j in range(0, i):

            # If arr[i] is greater, then
            # check with las[j][1]
            if (arr[j] < arr[i] and
                    las[i][0] < las[j][1] + 1):
                las[i][0] = las[j][1] + 1

            # If arr[i] is smaller, then
            # check with las[j][0]
            if (arr[j] > arr[i] and
                    las[i][1] < las[j][0] + 1):
                las[i][1] = las[j][0] + 1

        # Pick maximum of both values at index i
        if (res < max(las[i][0], las[i][1])):
            res = max(las[i][0], las[i][1])

    return res


# Driver Code
arr = [5,3,1,2,5]
n = len(arr)


def findMaxSumSubsequence(nums):
    n = len(nums)

    # base case
    if n == 0:
        return 0

    # base case
    if n == 1:
        return nums[0]

    # create an auxiliary space to store solutions to subproblems
    lookup = [None] * n

    # lookup[i] stores the maximum sum possible till index `i`

    # trivial case
    lookup[0] = nums[0]
    lookup[1] = max(nums[0], nums[1])

    # traverse list from index 2
    for i in range(2, n):
        # lookup[i] stores the maximum sum we get by

        # 1. Excluding the current element and take maximum sum until index `i-1`
        # 2. Including the current element nums[i] and take the maximum sum until
        #    index `i-2`
        lookup[i] = max(lookup[i - 1], lookup[i - 2] + nums[i])

        # if the current element is more than the maximum sum until the current
        # element
        lookup[i] = max(lookup[i], nums[i])

    # return maximum sum
    return lookup[n - 1]
# This code is contributed by divyesh072019
nums = [1, 2, 9, 4, 5, 0, 4, 11, 6]
print(findMaxSumSubsequence(nums))