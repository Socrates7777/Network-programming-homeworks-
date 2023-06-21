
#Convert from Binary to Decimal
decimal_number=0 #creating a variable and make it  0
binary_number=input('Enter your binary number:') # asking the user to enter a binary number
for num in binary_number: #going through each num in binary_number using for
    decimal_number=decimal_number*2 + int(num) #i did multipy the current value of decimal with 2 and add it to num
print("the equivalint of the binary in decimal",binary_number,"is",decimal_number)