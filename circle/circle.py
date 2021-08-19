from math import ceil, floor

xc, yc, *_  = input("Enter the circle center xc yc: ").split()
r = input("Enter the radius: ")

xc, yc, r = [int(n) for n in [xc,yc,r]]
x0, y0 = 0, r
print("**********"*7)

print("Solution:")
print(f"Given,\ncenter(xc,yc)=({xc},{yc})\nradius(r)={r}")
print("Step 1")
print(f"First point of circle center at origin (0, r)=(0,{r})")
print("Step 2")
print("Calculate initial decision parameter:")
print(f"p0 = 5/4 - r  but we take 5/4 as 1: po = 5/4 - {r} = {5/4-r}")
print(f"p0 = 1 - r = 1 - {r} = {1-r}")
print("if pk<0\t\t\t\tif pk>=0")
print("\txk+1 = xk +1\t\t\txk+1 = xk + 1")
print("\tyk+1 = yi\t\t\tyk+1 = yk - 1")
print("\tpk+1 = pk + 2xk+1 + 1\t\t\tpi+1=pi + 2xk+1 + 1 - 2yk+1")
def p0_less(xi, yi, pi):
    xnext = xi + 1
    ynext = yi
    pnext = pi + 2*xnext + 1
    return (xnext, ynext, pnext)

def p0_large(xi, yi, pi):
    # 2*xnext = 2xi + 2         2*ynext = 2yi - 2
    xnext = xi + 1
    ynext = yi - 1
    pnext = pi + 2*xnext + 1 - 2*ynext
    return (xnext, ynext, pnext)

def find_octant(x,y):
    return ((x,y),(x,-y),(-x,y),(-x,-y),(y,x),(y,-x),(-y,x),(-y,-x))

def change_center(x,y,xc,yc):
    x=x+xc
    y=y+yc
    return (x,y)

def circle(xc, yc, r):
    xi = 0
    yi = r
    p0 = 1 - r
    step = 0
    pi = p0
    xy = []
    print("Step 3:", "Table to find x,y coordinate")
    print("**********"*7)
    print("Step\tpk\txk\tyk\txk+1\tyk+1\tpk+1\t2*xk+1\t2*yk+1")
    while True:
        if pi < 0:
            xnext, ynext, pnext = p0_less(xi, yi, pi)
        else:
            xnext, ynext, pnext = p0_large(xi, yi, pi)
        print(f"{step}\t{pi}\t{xi}\t{yi}\t{xnext}\t{ynext}\t{pnext}\t{2*xnext}\t{2*ynext}")
        xy.append((xi,yi)) 
        xi = xnext
        yi = ynext
        pi = pnext
        step += 1
        if xnext >= ynext:
            break
    print("Step 4:", "Finding other 7 octates")
    print("**************"*9)
    print("(x,y)=(x+xc,y+yc)")
    print("(x,y)\t\t(x,-y)\t\t(-x,y)\t\t(-x,-y)\t\t(y,x)\t\t(y,-x)\t\t(-y,x)\t\t(-y,-x)")
    print("**************"*9)
    for i in xy:
        x, y = change_center(i[0], i[1], xc, yc)
        for j in find_octant(x, y):
            print(f"({j[0]:.1f},{j[1]:.1f})", end='\t')
        print()


print("**********"*7)
circle(xc, yc, r)

