from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    temp = deque(numbers)
    numbers.clear()
    temp.rotate(step)
    numbers[:] = [c for c in temp]


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)
