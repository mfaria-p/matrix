# Enter the Matrix — Notes

## Project structure

```
matrix/
  vector.py   — Vector class (all vector methods live here)
  matrix.py   — Matrix class (all matrix methods live here)
  ex00.py     — add, sub, scl
  ex01.py     — linear_combination
  ex02.py     — lerp
  ex03.py     — dot product
  ex04.py     — norm
  ex05.py     — cosine similarity
```

Each exercise imports from `vector.py` and/or `matrix.py`. Run any exercise with `python ex##.py`.

---

## Python basics used throughout

**`self.data`** — every object stores its numbers in a plain Python list called `data`. It's created in `__init__` and accessible anywhere as `obj.data`.

**`self.data = list(data)`** — the `list()` call makes a copy. Without it, two vectors would share the same list and mutating one would corrupt the other.

**`-> None`** — a type hint meaning "this function returns nothing." Python returns `None` automatically if there's no `return` statement. It's documentation, not instruction.

**`@classmethod` / `from_list`** — an alternative constructor. `Vector.from_list([1., 2.])` does the same thing as `Vector([1., 2.])`. The `cls` argument receives the class itself instead of an instance, so it works correctly even if you subclass `Vector`.

**In-place mutation** — `add`, `sub`, `scl` all modify `self.data` directly and return `None`. The caller does `u.add(v)` and `u` itself changes. Never return a new object from these.

---

## Exercise 00 — Add, Sub, Scale

Vector and Matrix operations that modify in place.

**Math:**
```
[2]   [5]   [7]          [2]       [4]
[3] + [7] = [10]   2  ×  [3]   =   [6]
```

**Key point:** you can only add vectors/matrices of the same size. Each component pairs with the one at the same position.

**Common mistakes:**
- Returning a new object instead of modifying `self`
- On Matrix: writing `self.data[i] += m.data[i]` — this concatenates rows (lists), not numbers. Always use `self.data[i][j]`.

---

## Exercise 01 — Linear Combination

```python
linear_combination(e: list[Vector], coefs: list[float]) -> Vector
```

Scale each vector by its coefficient, then sum them all.

**Math:**
```
10×[1,0,0] + (-2)×[0,1,0] + 0.5×[0,0,1] = [10, -2, 0.5]
```

**Key point:** always work on copies of the vectors in `e`. If you call `scl` directly on `e[i]`, you destroy the original.

Start from a zero vector of the right size:
```python
result = Vector([0.] * e[0].size())
```

---

## Exercise 02 — Linear Interpolation (lerp)

```python
lerp(u, v, t: float) -> same type as u and v
```

Returns the point that is `t` of the way from `u` to `v`. Works for floats, Vectors, and Matrices.

**Formula:**
```
lerp(u, v, t) = u + t × (v - u)
```

- `t = 0` → returns `u`
- `t = 1` → returns `v`
- `t = 0.5` → midpoint

**Matrix example** (`t = 0.5`):
```
v - u:   [[18, 9], [27, 36]]
t×(v-u): [[9, 4.5], [13.5, 18]]
result:  [[11, 5.5], [16.5, 22]]
```

Every element goes through the same formula independently.

**Key point:** work on copies of `u` and `v` — the methods mutate in place.

---

## Exercise 03 — Dot Product

```python
def dot(self, v: 'Vector') -> float
```

Multiply matching components, sum the results. Returns a single number.

**Math:**
```
[1, 2, 3] · [4, 5, 6] = (1×4) + (2×5) + (3×6) = 32
```

**Why it matters:**
- `u · v = 0` means the two vectors are perpendicular (orthogonal)
- The larger the dot product, the more aligned the two vectors are
- Negative dot product means they point away from each other

---

## Exercise 04 — Norm

Three methods measuring the vector's "length" in different ways.

**`norm_1` — Manhattan:** sum of absolute values of all components.
```
[1, -2, 3]  →  |1| + |-2| + |3|  =  6
```
Called "Manhattan" because it's like walking city blocks — no diagonals, only along axes.

**`norm` — Euclidean:** square each component, sum, take the square root. The actual geometric length, as if the vector's lenght measured with a ruler.
```
[1, -2, 3]  →  √(1² + 4 + 9)  =  √14  ≈  3.742
```

**`norm_inf` — Supremum:** the largest absolute value among all components.
```
[1, -2, 3]  →  max(1, 2, 3)  =  3
```

**No math library:** use `** 0.5` instead of `math.sqrt` — same result, no import needed.

**Absolute value without `abs()`:**
```python
absval = x if x >= 0 else -x
```

---

## Exercise 05 — Cosine Similarity

```python
def angle_cos(u: Vector, v: Vector) -> float
```

Returns the cosine of the angle between two vectors.

**Formula:**
```
cos(θ) = (u · v) / (‖u‖ × ‖v‖)
```

Just dot product divided by the product of both norms. One line — the work was already done in Ex03 and Ex04.

**What the result means:**
- `1`  → same direction (angle = 0°)
- `0`  → perpendicular (angle = 90°)
- `-1` → opposite directions (angle = 180°)

This is why cosine similarity is so useful — it tells you the angle without you having to compute it explicitly.

**Floating point note:** you may get `-0.9999999999999998` instead of `-1.0`. That's normal precision loss, not a bug.

---

### Bonus concept — Pearson Correlation

Pearson correlation is cosine similarity applied to **mean-centered** vectors.

**Centering** means subtracting the mean from every component:
```
u = [2, 4, 6]   →   mean = 4   →   centered = [-2, 0, 2]
```
The shape is identical — ups and downs are the same — but the average is now 0. You're no longer saying "this value is 6", you're saying "this value is 2 above average."

**Pearson formula:**
```
centered_u = u - mean(u)
centered_v = v - mean(v)
pearson(u, v) = angle_cos(centered_u, centered_v)
```

**What it tells you:** when one value goes up, does the other tend to go up too?
- `r = 1`  → perfect positive correlation
- `r = -1` → perfect negative correlation
- `r = 0`  → no linear relationship

**Key difference from cosine similarity:** cosine cares about direction of raw vectors. Pearson removes the offset first, so it only measures whether the *movements* are aligned — not the absolute levels.

```
u = [1, 2, 3]   centered = [-1, 0, 1]
v = [4, 5, 6]   centered = [-1, 0, 1]   →   pearson = 1.0
```
Different absolute values, identical relative movement → perfect correlation.
