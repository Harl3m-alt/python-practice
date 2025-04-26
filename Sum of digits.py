def sum_dig(i):
     total=0
     for i in str(i):
         total+=int(i)
     while i>0:
         total+=i%10
         i=i//10
     return total
 print(sum_dig(1234))
 print(sum_dig(1234))
