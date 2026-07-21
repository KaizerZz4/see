"""Tiny module the battery's CI exercises. Keep it trivial on purpose."""


def add(a: int, b: int) -> int:
    return a + b


def describe(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"
