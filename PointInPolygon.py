
from matplotlib import pyplot as plt


#check if the point is on the line
def on_and_between(pt1: tuple, pt3: tuple, pt2: tuple) -> bool:

    # simply check if x3 == x2 and if y3 lies between y1 and y2.
    x1, x2, x3 = pt1[0], pt2[0], pt3[0]
    y1, y2, y3 = pt1[0], pt2[0], pt3[0]
    #calculating slope of first two coords
    try:
        slope = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
       slope = 0

    pt3_on = (y3 - y1) == slope * (x3 - x1)
    pt3_between = (min(x1, x2) <= x3 <= max(x1, x2)) and (
        min(y1, y2) <= y3 <= max(y1, y2))

    if (pt3_on & pt3_between):
        return True

    return False

#Orientation is the relative arrangements of coords after a transformation or after traveling around a geometric figure.
#Ifyou’re given a problem to find out whether two line-segments intersect, there is an easy approach to this. It involves finding the orientation of the line segments. If they’re different, they intersect.
#https://blog.devgenius.io/clockwise-and-counterclockwise-line-segment-intersection-b3317839534e
#calculate orientation of three coords using slope
def orientation(pt1: tuple, pt2: tuple, pt3: tuple) -> int:

    val = (float(pt2[1] - pt1[1]) * (pt3[0] - pt2[0])) - \
        (float(pt2[0] - pt1[0]) * (pt3[1] - pt2[1]))

    if (val > 0):
        # Clockwise orientation
        return 1

    elif (val < 0):
        # Counterclockwise orientation
        return 2

    else:
        # Collinear orientation
        return 0


#check if line segments intersect using orientation
def Intersect(pt1, pt2, pt3, pt4):
#orientation for 4 cases i.e. 2 general and 2 special
#https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    orientation1 = orientation(pt1, pt2, pt3)
    orientation2 = orientation(pt1, pt2, pt4)
    orientation3 = orientation(pt3, pt4, pt1)
    orientation4 = orientation(pt3, pt4, pt2)

    # General case
    if (orientation1 != orientation2) and (orientation3 != orientation4):
        return True

    # Special Cases
    if (orientation1 == 0) and (on_and_between(pt1, pt3, pt2)):
        return True
    if (orientation2 == 0) and (on_and_between(pt1, pt4, pt2)):
        return True
    if (orientation3 == 0) and (on_and_between(pt3, pt1, pt4)):
        return True
    if (orientation4 == 0) and (on_and_between(pt3, pt2, pt4)):
        return True
    return False




def isInside(coords: list, p: tuple) -> bool:

    n = len(coords)
    if n < 3:
        print("not a ploygon")
        return False

    # Create a point for line segment from p to infinite
    extreme = (100, p[1])
    intersectCount = i = 0

    while True:
        next = (i + 1) % n
        if (Intersect(coords[i],
                        coords[next],
                        p, extreme)):

            if orientation(coords[i], p,
                           coords[next]) == 0:
                return on_and_between(coords[i], p,
                                      coords[next])
            intersectCount += 1
        i = next
        if (i == 0):
            break

    return (intersectCount % 2 == 1)



if __name__ == '__main__':
    polygon = [(0, 0), (10, 0), (10, 10), (0, 10), (2, 6), (8, 6)]
    polygon.append(polygon[0])
    xs, ys = zip(*polygon)
    plt.figure()
    plt.plot(xs, ys)
    p = (4, 2)
    plt.plot(4, 2, 'ro')
    plt.axhline(y=2, color='r', linestyle='dashed')
    plt.show()
    if (isInside(coords=polygon, p=p)):
      print('Inside the Polygon')
    else:
      print('Outside the Polygon')
