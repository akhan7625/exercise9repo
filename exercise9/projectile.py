from math import tan, pi, cos

g = 9.81
v0 = 44
deg = 80
x = 0.5
y0 = 1

theta = deg * (pi / 180)

y = y0 + x * tan(theta) - (g * x ** 2) / (2 * (v0 * cos(theta)) ** 2)

print(y)

# how do i make it print units?

