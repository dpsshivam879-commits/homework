# Take input values from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

# Sorting using swapping logic
if a > b:
    temp = a
    a = b
    b = temp

if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

# Displaying results
print("Values in ascending order:")
print("a =", a)
print("b =", b)
print("c =", c)