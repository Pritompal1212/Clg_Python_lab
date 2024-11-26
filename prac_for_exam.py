# def large(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
    
# a=54
# b=8
# c=32
# print(large(a,b,c))


# l=1
# u=10
# for i in range(l,u+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
            

# def swap(x,y):
#     a= x,y=y,x
#     return a
    
# x=1
# y=2
# print(swap(x,y))


a=50
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

a=2
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a%=2
print(a)

a=True
b=False
print(a and b)
print(a or b)
print(not b)

x = 5  # Binary: 0101
y = 3  # Binary: 0011

print("x & y (AND):", x & y)   # Output: 1 (Binary: 0001)
print("x | y (OR):", x | y)    # Output: 7 (Binary: 0111)
print("x ^ y (XOR):", x ^ y)   # Output: 6 (Binary: 0110)
print("~x (NOT):", ~x)         # Output: -6
print("x << 1 (Left Shift):", x << 1)  # Output: 10
print("x >> 1 (Right Shift):", x >> 1) 