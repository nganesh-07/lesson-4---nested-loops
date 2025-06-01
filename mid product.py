num = int(input("enter a number:"))
t = num
num_len = 0

while t > 0:
    num_len = num_len + 1
    t = int(t/10)

if num_len >= 4:
    num_len = int(num_len/2)
    chk = 0
    while num > 0:
        remainder = num % 10
        if chk == num_len:
            mid_one = remainder
        elif chk == num_len - 1:
            midtwo = remainder
        num = int(num/10)
        chk = chk + 1
    product = mid_one * midtwo
    print("Product of mid digits (" +str(mid_one)+ "*" +str(midtwo)+ ") = ", product)
else:
    print("It's not a 4 or more digit number.")

