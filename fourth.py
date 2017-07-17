#For-Loop and One-Parameter-Range Exercise

#This first loop will just print numbers from 0 to 4
print "FIRST LOOP"

for number in range(5):
	print number



#This second loop will sum the numbers from 0 to 4
#and will print the final sum
print "SECOND LOOP"

sum = 0

for number in range(5):
	sum = sum + number
	#sum += number
	
print sum