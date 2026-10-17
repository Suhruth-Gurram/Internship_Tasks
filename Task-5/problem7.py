#Symmetric Difference
#https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))
result=sorted(a.symmetric_difference(b))
for i in result:
    print(i)
