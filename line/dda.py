from math import ceil, floor

x1, y1, *_ = input("Enter x1 y1: ").split()
x2, y2, *_ = input("Enter x2 y2: ").split()

x1, y1, x2, y2 = [int(n) for n in [x1,y1,x2,y2]]
if x2<x1 and y2<y1:
    x1,y1,x2,y2 = x2,y2,x1,y1

dx = x2-x1
dy = y2-y1

# slope calculation
if dx == 0:
    print("Error cannot divide by zero")
    exit(1)
m = dy/dx

print("**********"*5)

print("Solution:")
print(f"Given,\n(x1,y1)=({x1},{y1}),  (x2,y2)=({x2},{y2})")
print(f"Slope(m) = y2-y1/x2-x1 = {y2}-{y1}/{x2}-{x1} = {dy}/{dx} = {m:.3}")

def calc_point(xi, yi, x2, y2, x, y, step):
    xnext = 0
    ynext = 0
    print(f"xi\tyi\txi+1\tyi+1")
    for i in range(step):
        xnext = xi + x
        ynext = yi + y
        print(f"{xi:.2f}\t{yi:.2f}\t{xnext:.2f}\t{ynext:.2f}")
        xi = xnext
        yi = ynext

def dda(xi, yi, x2, y2, m):
    if (abs(m) < 1):
        print("CASE I: |m| < 1")
        print(f"xi+1 = xi + 1\nyi+1 = yi + m")
        print(f"Repeat dx:{dx} times")
        print("**********"*5)
        calc_point(xi, yi, x2, y2, 1, m, dx)
    else:
        print("CASE II: |m| > 1")
        print(f"xi+1 = xi + 1/m\nyi+1 = yi + 1")
        print(f"Repeat dy:{dy} times")
        print("**********"*5)
        calc_point(xi, yi, x2, y2, 1/m, 1, dy)


print("**********"*5)
dda(x1, y1, x2, y2, m)

