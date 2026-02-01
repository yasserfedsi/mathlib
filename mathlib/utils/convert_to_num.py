from typing import Union

Number = Union[int, float]


def to_number(value) -> Number:
    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str):
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            pass

    raise TypeError(f"Invalid numeric value: {value!r}")
