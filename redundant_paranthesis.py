'''
Description:
Given a string of balanced expression, find if it contains any redundant parenthesis or not.

A set of parenthesis are redundant if same expression is surrounded by unnecessary or multiple brackets. Print "Yes" if redundant else "No".


Constraints:
|expression| > 3


Example:
Input:

((a+b))

Output:

Yes


Explanation:
In the expression ((a+b)), the sun-expression (a+b) is surrounded by unnecessary (). So, the answer is "Yes".
solution-(python):'''
st=[]
s=input()
for i in s:
    if i=='(':
        st.append(i)
    if i=='+' or i=='-' or i=='/' or i=='%' or i=='*':
        if st!=[]:
            st.append(i)
    if i==')':
        if st==[]:
            print("No")
            exit(1)
        if st[-1]=='(':
            print("Yes")
            exit(1)
        while st[-1]!='(':
            st.pop(-1)
print('No')
