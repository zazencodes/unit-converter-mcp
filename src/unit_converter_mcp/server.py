"""Main MCP server using FastMCP."""

from fastmcp import FastMCP

from .tools import (
    VALID_LENGTH_UNITS,
    VALID_TEMPERATURE_UNITS,
    VALID_VOLUME_UNITS,
    VALID_WEIGHT_UNITS,
    convert_length_tool,
    convert_temperature_tool,
    convert_volume_tool,
    convert_weight_tool,
)

# Create the FastMCP server instance
app: FastMCP = FastMCP("Unit Converter MCP Server")


@app.tool()
def convert_temperature(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value: The temperature value to convert
        from_unit: Source unit (celsius, fahrenheit, kelvin)
        to_unit: Target unit (celsius, fahrenheit, kelvin)

    Returns:
        Dictionary with original value, converted value, and units
    """
    try:
        converted_value = convert_temperature_tool(value, from_unit, to_unit)
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": converted_value,
            "converted_unit": to_unit,
            "conversion_type": "temperature",
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}


@app.tool()
def convert_length(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert length between various units.

    Args:
        value: The length value to convert
        from_unit: Source unit (meter, kilometer, centimeter, millimeter, inch, foot, yard, mile)
        to_unit: Target unit (meter, kilometer, centimeter, millimeter, inch, foot, yard, mile)

    Returns:
        Dictionary with original value, converted value, and units
    """
    try:
        converted_value = convert_length_tool(value, from_unit, to_unit)
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": converted_value,
            "converted_unit": to_unit,
            "conversion_type": "length",
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}


@app.tool()
def convert_weight(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert weight between various units.

    Args:
        value: The weight value to convert
        from_unit: Source unit (kilogram, gram, pound, ounce, ton)
        to_unit: Target unit (kilogram, gram, pound, ounce, ton)

    Returns:
        Dictionary with original value, converted value, and units
    """
    try:
        converted_value = convert_weight_tool(value, from_unit, to_unit)
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": converted_value,
            "converted_unit": to_unit,
            "conversion_type": "weight",
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}


@app.tool()
def convert_volume(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert volume between various units.

    Args:
        value: The volume value to convert
        from_unit: Source unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce)
        to_unit: Target unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce)

    Returns:
        Dictionary with original value, converted value, and units
    """
    try:
        converted_value = convert_volume_tool(value, from_unit, to_unit)
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": converted_value,
            "converted_unit": to_unit,
            "conversion_type": "volume",
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}


@app.tool()
def list_supported_units() -> dict:
    """List all supported units for each conversion type.

    Returns:
        Dictionary with supported units for each conversion type
    """
    return {
        "temperature": VALID_TEMPERATURE_UNITS,
        "length": VALID_LENGTH_UNITS,
        "weight": VALID_WEIGHT_UNITS,
        "volume": VALID_VOLUME_UNITS,
    }


def main() -> None:
    """Main entry point for the MCP server."""
    app.run()


if __name__ == "__main__":
    main()
