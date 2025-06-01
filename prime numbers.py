lower = int(input("Enter a lower number for your range here:"))
upper = int(input("Enter a higher number for your range here:"))

print("The prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
