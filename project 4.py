decimal = float(input("Enter any decimal number here:"))

if decimal==0:
    binary = "0"
else:
    binary = ""
    while decimal > 0:
        remainder = decimal%2
        binary = str(remainder) + binary
        decimal = decimal // 2

print("The binary version of your number is", binary)