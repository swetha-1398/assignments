num=int(input("enter the value of n:"))
if num<0:
  print("enter a positive number")
else:
  sum=0
  while(num>0):
     sum+=num
     num-=1
     print("the sum is",sum)