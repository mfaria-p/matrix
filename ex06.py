from vector import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    a = u.data
    b = v.data
    return Vector([
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ])


if __name__ == "__main__":
    u = Vector.from_list([0., 0., 1.])
    v = Vector.from_list([1., 0., 0.])
    print(cross_product(u, v))

    u = Vector.from_list([1., 2., 3.])
    v = Vector.from_list([4., 5., 6.])
    print(cross_product(u, v))

    u = Vector.from_list([4., 2., -3.])
    v = Vector.from_list([-2., -5., 16.])
    print(cross_product(u, v))
