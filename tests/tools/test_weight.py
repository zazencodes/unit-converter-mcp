"""Tests for weight conversion functions."""

import pytest

from unit_converter_mcp.tools.weight import convert_weight_tool


class TestWeightConversion:
    """Test weight conversion functions."""

    def test_kilogram_to_gram(self):
        """Test kilogram to gram conversion."""
        result = convert_weight_tool(1, "kilogram", "gram")
        assert result == 1000.0

    def test_pound_to_kilogram(self):
        """Test pound to kilogram conversion."""
        result = convert_weight_tool(1, "pound", "kilogram")
        assert abs(result - 0.453592) < 0.001

    def test_ounce_to_gram(self):
        """Test ounce to gram conversion."""
        result = convert_weight_tool(1, "ounce", "gram")
        assert abs(result - 28.3495) < 0.001

    def test_invalid_unit(self):
        """Test invalid weight unit."""
        with pytest.raises(ValueError):
            convert_weight_tool(100, "kilogram", "invalid_unit")
