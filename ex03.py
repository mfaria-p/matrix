from vector import Vector

if __name__ == "__main__":
    u = Vector.from_list([0., 0.])
    v = Vector.from_list([1., 1.])
    print(u.dot(v))

    u = Vector.from_list([1., 1.])
    v = Vector.from_list([1., 1.])
    print(u.dot(v))

    u = Vector.from_list([-1., 6.])
    v = Vector.from_list([3., 2.])
    print(u.dot(v))
