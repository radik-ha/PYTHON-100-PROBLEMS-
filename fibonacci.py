#Fibonacci series
print("Normal method")
n = 10
a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c

print("Using Function")

def fibo(m):
    x,y = 3,4
    for i in range(n):
        print(x)
        x,y = y,x+y
fibo(14)
