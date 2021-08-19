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

def calc_point_x(xi, yi, x2, y2, step):
    pi = 0
    pi1 = 0
    xi1 = 0
    yi1 = 0
    # repeat dx times
    pi = 2*dy - dx
    #print("if pi < 0\t\t\tif pi >= 0")
    print("\txi+1 = xi + 1\t\t\txi+1 = xi + 1")
    print("\tyi+1 = yi\t\t\tyi+1= yi + 1")
    print()
    print(f"steps\tpi\txi\tyi\txi+1\tyi+1\tpi+1")
    for i in range(step):
        if pi < 0:
            # print(f"pi+1 = pi + 2*dy")
            pi1 = pi + 2*dy
            xi1 = xi + 1
            yi1 = yi
        else:
            # print(f"pi+1 = pi + 2*dy - 2*dx")
            pi1 = pi + 2*dy - 2*dx
            xi1 = xi + 1
            yi1 = yi + 1
        print(f"{i+1}\t{pi:.2f}\t{xi:.2f}\t{yi:.2f}\t{xi1:.2f}\t{yi1:.2f}\t{pi1:.2f}")
        pi = pi1
        xi = xi1
        yi = yi1

def calc_point_y(xi, yi, x2, y2, step):
    # repeat dy times
    pi = 0
    pi1 = 0
    xi1 = 0
    yi1 = 0
    pi = 2*dx - dy
    # print("if pi < 0\t\tif pi >= 0")
    print("\txi+1 = xi\t\t\txi+1 = xi + 1")
    print("\tyi+1 = yi + 1\t\t\tyi+1= yi + 1")
    print()
    print(f"steps\tpi\txi\tyi\txi+1\tyi+1\tpi+1")
    for i in range(step):
        if pi < 0:
            # print(f"pi+1 = pi + 2*dx")
            pi1 = pi + 2*dx
            xi1 = xi
            yi1 = yi + 1
        else:
            pi1 = pi + 2*dx - 2*dy
            xi1 = xi + 1
            yi1 = yi + 1
        print(f"{i+1}\t{pi:.2f}\t{xi:.2f}\t{yi:.2f}\t{xi1:.2f}\t{yi1:.2f}\t{pi1:.2f}")
        pi = pi1
        xi = xi1
        yi = yi1

def bla(xi, yi, x2, y2, m):
    if abs(m) < 1:
        print("slope(m) < 1")
        print("slope < 1 repeat dx times")
        print(f"p0 = 2*dy - dx = 2*{dy} - {dx}\np0 = {2*dy-dx} ")
        print("if p0 < 0\t\t\tif p0 >= 0")
        print(f"\tpi+1 = pi + 2*dy\t\tpi+1 = pi + 2*dy - 2*dx")
        calc_point_x(xi, yi, x2, y2, dx)
    else:
        print("slope(m) >= 1")
        print("slope < 1 repeat dy times")
        print(f"p0 = 2*dx - dy = 2*{dx} - {dy}\np0 ={2*dx-dy} ")
        print("if p0 < 0\t\t\tif p0 >= 0")
        print(f"\tpi+1 = pi + 2*dx\t\tpi+1 = pi + 2*dx - 2*dy")
        calc_point_y(xi, yi, x2, y2, dy)


print("**********"*5)
bla(x1, y1, x2, y2, m)

