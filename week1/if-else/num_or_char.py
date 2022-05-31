# 3. WAP to find whether given input is number or character.

entered_input = input('Enter number or character: ')

if entered_input.isdigit():
    print ('Number')
elif entered_input.isalpha():
    print ('Alphabet character')
else:
    print ('Input is either alphanumeric or contain special character')