import math,random

length = 100000

#the path generation
path = ""

for i in range(length):
	if random.random() < .75:
		path += random.choice("LR")
	else:
		path += random.choice("123456789")

#initialize the origin
posx = 0
posy = 0

#initialize other variables
maxdistance = 0#the maximum distance from the origin to the furthest point on the path
currentdistance = 0#the distance from the origin to the current point on the path
direction = "N"#begin facing North
obstacle = False#obstacle is not present

#the array of obstacles
x = [(-10,46),(7,30),(92,240),(143,246),(240,382),(253,397),(274,466),(275,370),(307,469),(385,511)]

for c in path:
	'''#limit of the X,Y coordinate plan
	if posx < -100000:
		posx = -100000
	elif posx > 100000:
		posx = 100000
	elif posy < -100000:
		posy = -100000
	elif posy > 100000:
		posy = 100000'''
	if c == "L":#direction is Left
		if direction == "N":
			 direction = "W"
		elif direction == "W":
			 direction = "S"
		elif direction == "S":
			 direction = "E"
		else:
			 direction = "N"
	elif c == "R":#direction is Right
		if direction == "N":
			 direction = "E"
		elif direction == "W":
			 direction = "N"
		elif direction == "S":
			 direction = "W"
		else:
			 direction = "S"
	else:#c in ["1","2","3","4","5","6","7","8","9"]: move 1-9 units
		if direction == "N":#move North
			for a,b in x:
				if posx == a and b-posy-int(c) <= 0 and b > posy:
					obstacle = True
					break;
			if obstacle:
				posy = b - 1
				obstacle = False
			else:
				posy = posy + int(c) 
			currentdistance = math.sqrt(posx*posx + posy*posy)
		elif direction == "W":#move West
			for a,b in x:
				if posy == b and posx-a-int(c) <= 0 and a < posx:
					obstacle = True
					break;
			if obstacle:
				posx = a + 1
				obstacle = False
			else:
				posx = posx + -int(c)
			currentdistance = math.sqrt(posx*posx + posy*posy)
		elif direction == "S":#move South
			for a,b in x:
				if posx == a and posy-b-int(c) <= 0 and b < posy:
					obstacle = True
					break;
			if obstacle:
				posy = b + 1
				obstacle = False
			else:
				posy = posy + -int(c)
			currentdistance = math.sqrt(posx*posx + posy*posy)
		else:#move East
			for a,b in x:
				if posy == b and a-posx-int(c) <= 0 and a > posx:
					obstacle = True
					break;
			if obstacle:
				posx = a - 1
				obstacle = False
			else:
				posx = posx + int(c) 
			currentdistance = math.sqrt(posx*posx + posy*posy)
		if currentdistance > maxdistance:
			maxdistance = currentdistance
print(round(maxdistance,2))
