from core import Vector as _RustVector


class Vector:
    """High-level Vector API backed by Rust core."""

    def __init__(self, data):
        self._vec = _RustVector(data)

    def __repr__(self):
        return repr(self._vec)

    def add(self, other: "Vector") -> "Vector":
        result = self._vec.add(other._vec)
        
        new_vec = Vector.__new__(Vector)
        new_vec._vec = result

        return new_vec

    def dot(self, other: "Vector") -> float:
        return self._vec.dot(other._vec)

    def __add__(self, other: "Vector") -> "Vector":
        return self.add(other)
