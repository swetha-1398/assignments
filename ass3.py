n=int(input("Enter the amount:"))
if n>=1000:
thousands=n/1000
print("1000:",note1000)
n=n%1000
if n>=500:
five hundreds=n/500
print("500:",note500)
n=n%500
if n>=100:
hundreds=n/100
print("100:",note100)
n=n%100
if n>=50:
fifty=n/50
print("50:",note50)
n=n%50
if n>=10:
tens=n/10
print("10:",note10)
n=n%10
if n>=5:
five rupees=n/5
print("5:",note5)
n=n%5
if n>=2:
two rupees=n/2
print("2:",note2)
n=n%2
if n>=1:
ones=n/1
print("1:",note1)