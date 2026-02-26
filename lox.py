


x1 = -2
x2 = 3
dx = 1
a = -1
b = 2
c = 1


print("x"," " * 15, "F(x)" )
print("")

for x in range(x1, x2 + 1, dx):
    if c > 0 and x > 0:
        F = b * x / c
    if a < 0:
        F = a * (x ** 2)
    else:
        F = (a + b) * x - c

    print(x, " " * 15, F)


