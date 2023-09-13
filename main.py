from point import Point
def main():

    p1 = Point(3,4)
    p2 = Point(2,4)

    # print(p1 == p2)
    #  return false. because the operator cannot compare objects

    # print(p1)
    # return an unreadable string of the location object.

    # print(p1 + p2)
    # unsupported operand type- which means it cannot add two objects.  

    print(p1)
    print(p1+p2)
    print(p1==p2)


if __name__ == '__main__':
    main()