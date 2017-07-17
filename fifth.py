#For-Loop and Two-Parameters-Range Function Exercise

#This first loop will go over the numbers 97 to 122 and print them as well
#as the letters a to z they represent in the ascii table  
print "---Using the chr() function---"

for number in range(97, 123):
	print "Ascii Decimal -->",
	print number,
	
	print chr(number),
	print "<-- Character"


#This second loop will go over the letters from a to z and print them as well
#as the numbers 97 to 122 they are represented with in the ascii table
print "---Using the ord() function---"

for letter in "abcdefghijklmnopqrstuvwxyz":
	print "Character -->",
	print letter,
	
	print ord(letter),
	print "<-- Ascii Decimal"
