from vector import Vector
from matrix import Matrix


def lerp(u, v, t: float):
    if isinstance(u, (int, float)):
        return u + t * (v - u)
    start = type(u)(u.data)
    end   = type(v)(v.data)
    end.sub(start)   # end = v - u
    end.scl(t)       # end = t * (v - u)
    start.add(end)   # start = u + t*(v-u)
    return start


if __name__ == "__main__":
    print(lerp(0., 1., 0.))
    print(lerp(0., 1., 1.))
    print(lerp(0., 1., 0.5))
    print(lerp(21., 42., 0.3))

    print(lerp(Vector.from_list([2., 1.]), Vector.from_list([4., 2.]), 0.3))
    print(lerp(
        Matrix.from_list([[2., 1.], [3., 4.]]),
        Matrix.from_list([[20., 10.], [30., 40.]]),
        0.5
    ))
