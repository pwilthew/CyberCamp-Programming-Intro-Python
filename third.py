#User Input and If-Statement Exercise

number = raw_input("Enter a number: ")

#Because raw_input saves input as a string, we need to convert it to integer
number = int(number)

if number < 10:
    print "The number is less than 10."

elif number == 10:
    print "The number is equal to 10."

elif number > 10:
    print "The number is greater than 10."
