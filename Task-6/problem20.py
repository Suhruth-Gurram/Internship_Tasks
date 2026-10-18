#Validating phone numbers

#https://www.hackerrank.com/challenges/validating-the-phone-number/problem


n = int(input())

for i in range(n):
    s = input()

    if len(s) == 10 and s.isdigit() and (s[0] == '7' or s[0] == '8' or s[0] == '9'):
        print("YES")
    else:
        print("NO")
