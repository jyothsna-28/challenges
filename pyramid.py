'''
Write a program to print  Full Pyramid of *


Constraints:
NA


Example:
NA


Explanation:
NA


Public Test Cases:
#
INPUT	
4
EXPECTED OUTPUT	
      * 
    * * * 
  * * * * * 
* * * * * * * 
solution-(python):
'''
n=int(input())
for i in range(n):
    print("  "*(n-i-1),"* "*(2*i+1),sep="")
