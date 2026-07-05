from vector import Vector

if __name__ == "__main__":
    u = Vector.from_list([0., 0., 0.])
    print(u.norm_1(), u.norm(), u.norm_inf())

    u = Vector.from_list([1., 2., 3.])
    print(u.norm_1(), u.norm(), u.norm_inf())

    u = Vector.from_list([-1., -2.])
    print(u.norm_1(), u.norm(), u.norm_inf())
