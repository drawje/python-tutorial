students = ["egoing","sori","maru"]
grades = [2,1,4]
print("students[1]", students[1])
print("len(students)",len(students))
print("min(grades)",min(grades))
print("max(grades)",max(grades))
print("sum(grades)",sum(grades))

import statistics #통계와 관련된 모듈
print("statistics.mean(grades)",statistics.mean(grades))

import random
print("random.choice(students)",random.choice(students))  #랜덤으로 선택을 함