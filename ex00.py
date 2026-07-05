from vector import Vector
from matrix import Matrix

if __name__ == "__main__":
    print("=== Vector add ===")
    u = Vector.from_list([2., 3.])
    v = Vector.from_list([5., 7.])
    u.add(v)
    print(u)

    print("\n=== Vector sub ===")
    u = Vector.from_list([2., 3.])
    v = Vector.from_list([5., 7.])
    u.sub(v)
    print(u)

    print("\n=== Vector scl ===")
    u = Vector.from_list([2., 3.])
    u.scl(2.)
    print(u)

    print("\n=== Matrix add ===")
    u = Matrix.from_list([[1., 2.], [3., 4.]])
    v = Matrix.from_list([[7., 4.], [-2., 2.]])
    u.add(v)
    print(u)

    print("\n=== Matrix sub ===")
    u = Matrix.from_list([[1., 2.], [3., 4.]])
    v = Matrix.from_list([[7., 4.], [-2., 2.]])
    u.sub(v)
    print(u)

    print("\n=== Matrix scl ===")
    u = Matrix.from_list([[1., 2.], [3., 4.]])
    u.scl(2.)
    print(u)
