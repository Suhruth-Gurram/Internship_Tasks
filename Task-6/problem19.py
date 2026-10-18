#Company Logo
#https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()
    count = Counter(s)

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for ch, freq in result[:3]:
        print(ch, freq)
