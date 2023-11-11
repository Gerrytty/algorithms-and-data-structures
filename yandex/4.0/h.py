import math

a = int(input())
b = int(input())
n = int(input())

min_student_in_b = math.ceil(b/n)

if min_student_in_b == 0 and b != 0:
	min_student_in_b = 1

if a > min_student_in_b:
	print("Yes")
else:
	print("No")