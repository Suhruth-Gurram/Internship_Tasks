#Word Order
#https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
for i in range(n):
    words.append(input())
unique = []
for i in words:
    if i not in unique:
        unique.append(i)
print(len(unique))
for i in unique:
    print(words.count(i), end=" ")
