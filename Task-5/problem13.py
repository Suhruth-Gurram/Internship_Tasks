#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(set(s[1] for s in students))
    for s in sorted(students):
        if s[1] == scores[1]:
            print(s[0])
