num=int(input("enter a number:"))
if num>1:
 for i in range(2,num//2):
   if(num%i)==0:
    print(num,"it is not a prime number")
 else:
    print(num,"it is a prime number")
else:
    print(num,"it is not a prime number")
