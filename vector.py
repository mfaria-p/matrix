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
