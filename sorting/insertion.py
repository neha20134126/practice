#program for insertion sort
from array import array
number = input()

intarray = array('i')
for i in range(0, number) :
	num = input()
	intarray.append(num)

for i in range(0, number) :
	key = intarray[i]
	j = i-1
	while j >=0 and key < intarray[j]:
		intarray[j+1] = intarray[j]
		j -= 1
	intarray[j+1] = key

print "sorted array is"
for i in range(0, number):
	print intarray[i]
