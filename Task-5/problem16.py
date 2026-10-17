#Collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem
n = int(input())
shoes = list(map(int, input().split()))
customers = int(input())
money = 0
for i in range(customers):
    size, price = map(int, input().split())
    if size in shoes:
        money += price
        shoes.remove(size)
print(money)
