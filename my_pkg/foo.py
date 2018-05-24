from shapely.geometry import Point
from my_pkg.module import bar

def foo():
    p = Point(0,0)
    return p.buffer(1)

if __name__ == '__main__':
    print foo()
