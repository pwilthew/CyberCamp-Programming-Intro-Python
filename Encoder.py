### THE FOLLOWING CODE ENCODES A PHRASE USING CAESARS' CIPHER 

# this constant (static variable) will determine the rotation.
# if set to one, each letter will rotate once. Ex: 'a' will be 'b'
SHIFT = 1

# this variable will get its value from user input
phrase = raw_input("Enter the phrase you want to encode: ")

# encoded_phrase will get its value later, but initially, 
# it is an empty string
encoded_phrase = ""

# this loop grabs each character from the phrase and rotates it
for char in phrase:

    # get the decimal representation of char
    char_in_decimal = ord(char)

    # if char_in_decimal represents a letter between 'a' and 'z', then shift it
    if char_in_decimal > ord('a') and char_in_decimal < ord('z'):

        # increment the letter by SHIFT places
        char_in_decimal = char_in_decimal + SHIFT 

        # if the shifted char_in_decimal is greater than 'z', which represents 122,
        # then substract 26 (number of letters in the abc)
        if char_in_decimal > ord('z'):
            char_in_decimal = char_in_decimal - 26

    # encoded_phrase will be formed by the concatenation of each new character
    encoded_phrase = encoded_phrase + chr(char_in_decimal)

print encoded_phrase
