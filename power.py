num = int(input("Enter the number of which you have to find power: "))
power = int(input("Enter the power: "))

r= 1
for n in range(power):
    r = r*num

print(r)