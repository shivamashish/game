#python program to display first n fibbonaci numbers using while loop
n=int(input("Enter a limit:"))
a=0
b=1
i=3
print("first",n,"fibbonaci series are as follows")
print(a,b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1

print("End of the program")
