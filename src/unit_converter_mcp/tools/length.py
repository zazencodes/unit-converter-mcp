"""Length conversion functions."""

from ..utils import Validator

VALID_LENGTH_UNITS = [
    "meter",
    "kilometer",
    "centimeter",
    "millimeter",
    "inch",
    "foot",
    "yard",
    "mile",
]

validator = Validator("length")


def convert_length_tool(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length between various units."""
    validator.validate_unit(from_unit, VALID_LENGTH_UNITS)
    validator.validate_unit(to_unit, VALID_LENGTH_UNITS)

    # Convert to meters first
    to_meters = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
    }

    meters = value * to_meters[from_unit]
    return meters / to_meters[to_unit]
