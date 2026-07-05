from vector import Vector


def angle_cos(u: Vector, v: Vector) -> float:
    return u.dot(v) / (u.norm() * v.norm())


if __name__ == "__main__":
    u = Vector.from_list([1., 0.])
    v = Vector.from_list([1., 0.])
    print(angle_cos(u, v))

    u = Vector.from_list([1., 0.])
    v = Vector.from_list([0., 1.])
    print(angle_cos(u, v))

    u = Vector.from_list([-1., 1.])
    v = Vector.from_list([ 1., -1.])
    print(angle_cos(u, v))

    u = Vector.from_list([2., 1.])
    v = Vector.from_list([4., 2.])
    print(angle_cos(u, v))

    u = Vector.from_list([1., 2., 3.])
    v = Vector.from_list([4., 5., 6.])
    print(angle_cos(u, v))
