#Prints the average of two random points in a 1x1 square

import math,random

def distance(x1,y1,x2,y2):
	X = x2 - x1
	Y = y2 - y1
	if X < 0:
		X = X * -1
	if Y < 0:
		Y = Y * -1
	return math.sqrt(X*X + Y*Y)

sum = 0
attempts = 100000

for i in range(attempts):
	sum = sum + distance(random.random(),random.random(),random.random(),random.random())


print(sum/attempts)
#Approximation of (2+sqrt(2) +5ln(sqrt(2)+1))/15 = 0.521405433164720678330982