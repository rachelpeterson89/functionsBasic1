# Challenge 1
def a():
    return 5
print(a())
# 5


# Challenge 2
def a():
    return 5
print(a()+a())
# 10


# Challenge 3
def a():
    return 5
    return 10
print(a())
# 5


# Challenge 4
def a():
    return 5
    print(10)
print(a())
# 5


# Challenge 5
def a():
    print(5)
x = a()
print(x)
# 5,none


# Challenge 6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# 3,5


# Challenge 7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# 25


# Challenge 8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# 100,10


# Challenge 9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# 7,14,21


# Challenge 10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# 8


# Challenge 11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# 500,500,300,500


# Challenge 12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# 500,500,300,500


# Challenge 13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# 500,500,300,300


# Challenge 14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# 1,3,2


# Challenge 15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# 1,3,5,10