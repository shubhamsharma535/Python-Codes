n = int(input("Enter the number: "))
a=0
b=1
sum=0
count=1
print("Fibonacci Series of the number is: " )
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b