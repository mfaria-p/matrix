class Matrix:
    def __init__(self, data: list):
        self.data = [list(row) for row in data]  # deep copy rows

    @classmethod
    def from_list(cls, data: list):
        return cls(data)

    def shape(self):
        return (len(self.data), len(self.data[0]))

    def is_square(self) -> bool:
        r, c = self.shape()
        return r == c

    def __repr__(self) -> str:
        return '\n'.join(str(row) for row in self.data)

    # --- Exercise 00 ---

    def add(self, m: 'Matrix') -> None:
        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] += m.data[i][j]

    def sub(self, m: 'Matrix') -> None:
        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] -= m.data[i][j]

    def scl(self, a) -> None:
        rows, cols = self.shape()
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] *= a
