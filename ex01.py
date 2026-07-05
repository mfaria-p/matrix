from vector import Vector


def linear_combination(e: list, coefs: list) -> Vector:
    result = Vector([0.] * e[0].size())
    for i in range(len(e)):
        scaled = Vector(e[i].data)
        scaled.scl(coefs[i])
        result.add(scaled)
    return result


if __name__ == "__main__":
    e1 = Vector.from_list([1., 0., 0.])
    e2 = Vector.from_list([0., 1., 0.])
    e3 = Vector.from_list([0., 0., 1.])
    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))

    v1 = Vector.from_list([1., 2., 3.])
    v2 = Vector.from_list([0., 10., -100.])
    print(linear_combination([v1, v2], [10., -2.]))
