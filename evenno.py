start=int(input("enter the startof range:"))
end=int(input("enter the end of the range"))
for num in range(start,end+1):
  if(num%2==0):
   print(num, end=" ")