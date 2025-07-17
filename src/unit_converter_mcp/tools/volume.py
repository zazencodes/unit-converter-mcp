"""Volume conversion functions."""

from ..utils import Validator

VALID_VOLUME_UNITS = [
    "liter",
    "milliliter",
    "gallon",
    "quart",
    "pint",
    "cup",
    "fluid_ounce",
]

validator = Validator("volume")


def convert_volume_tool(value: float, from_unit: str, to_unit: str) -> float:
    """Convert volume between various units."""
    validator.validate_positive_number(value)
    validator.validate_unit(from_unit, VALID_VOLUME_UNITS)
    validator.validate_unit(to_unit, VALID_VOLUME_UNITS)

    # Convert to liters first
    to_liters = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "fluid_ounce": 0.0295735,
    }

    liters = value * to_liters[from_unit]
    return liters / to_liters[to_unit]
