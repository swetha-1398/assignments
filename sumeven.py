n=int(input("enter n value:"))
i=1
sum=0
while i<n:
  if i%2==0:
    sum+=i
    i=i+1
    print("sum of even numbers",sum)