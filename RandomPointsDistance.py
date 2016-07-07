The average waiting time between consecutive Heads-Heads (HH) is longer than the average waiting time between Heads-Tails(HT)
import random
length = 50000
string = ""
HH = 0
HT = 0
index = 1
HHarray = []
HTarray = []
consecutive = False
for i in range(length):
 if random.random() < .5:
 string += "H"
 else:
 string += "T"
for i, j in zip(string[::1], string[1::1]):
 if i+j == "HH" and consecutive == False:
 HHarray.append(index)
 index += 1
 consecutive = True
 elif i+j == "HT":
 HTarray.append(index)
 index += 1
 consecutive = False
 else:
 index += 1
 consecutive = False
HHarray = [HHarray[0]] + [j-i for i, j in zip(HHarray[:-1], HHarray[1:])]
HTarray = [HTarray[0]] + [j-i for i, j in zip(HTarray[:-1], HTarray[1:])] 
print("The average waiting time of HH is " + str(sum(HHarray)/len(HHarray)))#Expected Value is 6
print("The average waiting time of HT is " + str(sum(HTarray)/len(HTarray)))#Expected Value is 4
#The average waiting time between consecutive Heads-Heads (HH) is longer than the average waiting time between Heads-Tails(HT)
import random
length = 50000
string = ""
HH = 0
HT = 0
index = 1
HHarray = []
HTarray = []
consecutive = False
for i in range(length):
 if random.random() < .5:
 string += "H"
 else:
 string += "T"
for i, j in zip(string[::1], string[1::1]):
 if i+j == "HH" and consecutive == False:
 HHarray.append(index)
 index += 1
 consecutive = True
 elif i+j == "HT":
 HTarray.append(index)
 index += 1
 consecutive = False
 else:
 index += 1
 consecutive = False
HHarray = [HHarray[0]] + [j-i for i, j in zip(HHarray[:-1], HHarray[1:])]
HTarray = [HTarray[0]] + [j-i for i, j in zip(HTarray[:-1], HTarray[1:])] 
print("The average waiting time of HH is " + str(sum(HHarray)/len(HHarray)))#Expected Value is 6
print("The average waiting time of HT is " + str(sum(HTarray)/len(HTarray)))#Expected Value is 4
