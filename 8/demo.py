import geometry

def PointyShapeVolume(x,h,sq):
    if sq:
        base=geometry.SquareArea(x)
    else:
        base=geometry.CircleArea(x)
    return h*base/3.0
print(PointyShapeVolume(4,2.8,True))
print(PointyShapeVolume(4,2.8,False))
