xc, yc, *_  = input("Enter the ellipse center xc yc: ").split()
rx, ry, *_ = input("Enter the radius along x-axis and y-axis rx ry: ").split()

xc, yc, rx, ry = [int(n) for n in [xc,yc,rx,ry]]
print("**********"*7)

print("Solution:")
print(f"Given,\ncenter(xc,yc)=({xc},{yc})\nradius(rx,ry)=({rx},{ry})")
print("Step 1")
print(f"First point of ellipse center at origin (0, ry)=(0,{ry})")
print("Step 2")
print("Calculate initial decision parameter:")
print(f"p0=ry^2+1/4*rx^2-rx^2*ry = {ry**2}+1/4*{rx**2}-{rx**2}*{ry}")
print(f"p0 = {ry**2+1/4*rx**2-rx**2*ry}")
print()
print("If p1k<0 then the next point along the is (xk+1 , yk) and pk+1=pk+2ry^2xk+1+ry2")
print("Else, the next point is (xk+1, yk-1) ")



def midptellipse(rx, ry, xc, yc):
    x = 0;
    y = ry;
    print(f"initial point,(x,y)=(0,ry)=(0,{ry})") 
 
    # Initial decision parameter of region 1
    d1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx);
    print(f"Initial decision parameter: p0 = {d1}")
    dx = 2 * ry * ry * x;
    dy = 2 * rx * rx * y;
 
    print("points based on 4-way symmetry for region 1")
    print(f"First Region d1\t\t(x,y)\t(-x,y)\t(x,-y)\t(-x,-y)")
    while (dx < dy):
        print(f"{d1:>15}\t\t{x+xc},{y+yc}\t{-x+xc},{y+yc}\t{x+xc},{-y+yc}\t{-x+xc},{-y+yc}")
        #print(f"{d1:.2f}",end="\t\t");
        #print("(", x + xc, ",", y + yc, ")",end="\t");
        #print("(", -x + xc, ",", y + yc, ")",end="\t");
        #print("(", x + xc, ",", -y + yc, ")",end="\t");
        #print("(", -x + xc, ",", -y + yc, ")");
        if (d1 < 0):
            x += 1;
            dx = dx + (2 * ry * ry);
            d1 = d1 + dx + (ry * ry);
        else:
            x += 1;
            y -= 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            d1 = d1 + dx - dy + (ry * ry);
 
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry));
 
    print("points based on 4-way symmetry for region 2")
    print("Second Region d2\t(x,y)\t(-x,y)\t(x,-y)\t(-x,-y)")
    while (y >= 0):
        print(f"{d2:>15}\t\t{x + xc},{y + yc}\t{-x + xc},{y + yc}\t{x + xc},{-y + yc}\t{-x + xc},{-y + yc}")
        #print(f"{d2:.2f}",end="\t\t");
        #print("(", x + xc, ",", y + yc, ")",end="\t");
        #print("(", -x + xc, ",", y + yc, ")",end="\t");
        #print("(", x + xc, ",", -y + yc, ")",end="\t");
        #print("(", -x + xc, ",", -y + yc, ")");
        #print("(", x + xc, ",", y + yc, ")");
        #print("(", -x + xc, ",", y + yc, ")");
        #print("(", x + xc, ",", -y + yc, ")");
        #print("(", -x + xc, ",", -y + yc, ")");
 
        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1;
            dy = dy - (2 * rx * rx);
            d2 = d2 + (rx * rx) - dy;
        else:
            y -= 1;
            x += 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            d2 = d2 + dx - dy + (rx * rx);
 
midptellipse(10, 15, 50, 50);
