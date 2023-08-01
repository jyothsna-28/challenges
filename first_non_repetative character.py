'''
Description:
Given a stream of characters (lowercase alphabets), find the first non-repeating character from stream. You need to tell the first non-repeating character in O(1) time at each index. If for a current index there is no such character return '0' for that particular index.

Input Format:

A String S of length N passed as a parameter to the given function.

Output Format:

Return a vector of characters of length N where V[i] character represents first non-repeating character from S[0] to S[i].


Constraints:
1<=N<=100

Expected time complexity:

O(N) where N is the total number of input characters in one testcase. (Use the property of queue)


Example:
Input:

aabcbcd

Output:

a 0 b b c 0 d


Explanation:
At index 0, 'a' is the only character we have and hence non repeating.

At index 1, we have 2 characters till now and they are same, hence no non-repeating character.

At index 2, 'b' is the only non repeating character till now.

At index 3, 'b' and 'c' are non repeating characters, but 'b' is the FIRST non repeating character till now.

At index 4, 'c' is the only non repeating character till now.

At index 5, there is no non repeating character till now.

At index 6, 'd' is the only and first non repeating character.
solution(python-3):'''
#reading input
s=input()
#initialize two emplty lists where r list will contain repetative characters and l will contain non-repetative characters 
l=[]
r=[]
#iterate each character using for loop
for i in s:
    flag=False
    if i not in l and i not in r:
        l.append(i)
        print(l[0],end="")
        flag=True
    elif i in l:
        r.append(i)
        l.remove(i)
        if l==[]:
            print(0,end="")
        else:
            print(l[0],end="")
