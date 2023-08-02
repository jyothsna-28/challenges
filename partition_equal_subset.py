'''
partition equal subset sum
The partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

If equal partition then return True otherwise false

Input:

Line 1: size of array

Line 2: elements

 

Output:

Line 1:Boolean(True or False)


Constraints:
1 <= arr.length <= 200

1 <= arr[i] <= 100


Example:
Example 1:

Input: nums = [1,5,11,5]

Output:True

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]

Output: False

Explanation: The array cannot be partitioned into equal sum subsets.


Explanation:
using dynamic programming


Public Test Cases:
#	INPUT	EXPECTED OUTPUT
1	
4
1 5 11 5
True
2	
4
1 2 3 5
False
3	
4
1 5 11 5
True
4	
1
0
True
solution-python:
'''
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i::]):
        print(True)
        exit(1)
print(False)
