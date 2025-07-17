"""Weight conversion functions."""

from ..utils import Validator

VALID_WEIGHT_UNITS = ["kilogram", "gram", "pound", "ounce", "ton"]

validator = Validator("weight")


def convert_weight_tool(value: float, from_unit: str, to_unit: str) -> float:
    """Convert weight between various units."""
    validator.validate_positive_number(value)
    validator.validate_unit(from_unit, VALID_WEIGHT_UNITS)
    validator.validate_unit(to_unit, VALID_WEIGHT_UNITS)

    # Convert to kilograms first
    to_kg = {
        "kilogram": 1.0,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "ton": 1000.0,
    }

    kg = value * to_kg[from_unit]
    return kg / to_kg[to_unit]
