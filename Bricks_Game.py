"""Problem

Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

Input:

First line contains an integer N.

Output:

Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.

Constraints:

1 ≤ N ≤ 10000
Sample Input

13

Sample Output

Motu

Time Limit: 1
Memory Limit: 256
Source Limit:
Explanation

Sample Explanation:

13 bricks are there :

Patlu Motu

1 2 """

# ************************************************ CODE **************************************************************

n = int(input())
i = 1
m = 0
p = 0
s = 0
res = ""
while(i<n):
    m = i
    s += m
    if(s>n):
        res = "Patlu"
        break

    p = i*2
    s += p
    if(s > n):
        res = "Motu"
        break
    i += 1

print(res)    

    
