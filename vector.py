class Vector:
    def __init__(self, data: list):
        self.data = list(data)  # deep copy

    @classmethod
    def from_list(cls, data: list):
        return cls(data)

    def size(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return '\n'.join(f'[{x}]' for x in self.data)

    # --- Exercise 00 ---

    def add(self, v: 'Vector') -> None:
        for i in range(self.size()):
            self.data[i] += v.data[i]

    def sub(self, v: 'Vector') -> None:
        for i in range(self.size()):
            self.data[i] -= v.data[i]

    def scl(self, a) -> None:
        for i in range(self.size()):
            self.data[i] *= a

    # --- Exercise 03 ---

    def dot(self, v: 'Vector') -> float:
        result = 0.
        for i in range(self.size()):
            result += self.data[i] * v.data[i]
        return result

    # --- Exercise 04 ---

    def norm_1(self) -> float:
        result = 0.
        for x in self.data:
            result += x if x >= 0 else -x
        return result

    def norm(self) -> float:
        result = 0.
        for x in self.data:
            result += x * x
        return result ** 0.5

    def norm_inf(self) -> float:
        result = 0.
        for x in self.data:
            absval = x if x >= 0 else -x
            if absval > result:
                result = absval
        return result
