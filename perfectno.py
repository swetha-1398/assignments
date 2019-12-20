def print_perfect_nums(start, end):
   for i in range(start, end + 1):
     sum1 = 0
   for x in range(1, i):
      if(i % x == 0):
         sum1 = sum1 + x
         if (sum1 == i):
            print(i)
print_perfect_nums(1, 300)