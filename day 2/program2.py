num = int(input("Enter the value of N: "))
a = 0
b = 1
print("The Fibonacci series upto", num, "th number is following: ")
for i in range(num):
    print(a,end = " ")
    c = a + b
    a = b
    b = c