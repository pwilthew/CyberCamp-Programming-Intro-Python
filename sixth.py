#While-Loop and String Concatenation Exercise

counter = 0
word = ""

#This while-loop will ask for a letter 5 consecutive times
#and will create a word by concatenating the letters together
while counter != 5:
    letter = raw_input("Enter one letter: ")
    word = word + letter
    counter = counter + 1

print word
