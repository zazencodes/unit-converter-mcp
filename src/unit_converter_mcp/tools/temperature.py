"""Temperature conversion functions."""

from ..utils import Validator

VALID_TEMPERATURE_UNITS = ["celsius", "fahrenheit", "kelvin"]

validator = Validator("temperature")


def convert_temperature_tool(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    validator.validate_unit(from_unit, VALID_TEMPERATURE_UNITS)
    validator.validate_unit(to_unit, VALID_TEMPERATURE_UNITS)

    if from_unit == "kelvin":
        validator.validate_positive_number(value)

    # Convert to Celsius first
    if from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:  # celsius
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:  # celsius
        return celsius
