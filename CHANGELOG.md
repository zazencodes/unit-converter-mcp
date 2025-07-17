# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-07-16

### Added
- Initial release of unit-converter-mcp
- FastMCP v2.0 server implementation
- Five unit conversion tools:
  - `convert_temperature` - Convert between Celsius, Fahrenheit, and Kelvin
  - `convert_length` - Convert between metric and imperial length units (meter, kilometer, centimeter, millimeter, inch, foot, yard, mile)
  - `convert_weight` - Convert between various weight/mass units (kilogram, gram, pound, ounce, ton)
  - `convert_volume` - Convert between metric and imperial volume units (liter, milliliter, gallon, quart, pint, cup, fluid_ounce)
  - `list_supported_units` - List all supported units for each conversion type
- Test suite with pytest covering all conversion tools
- Documentation with detailed examples and usage instructions
- PyPI packaging
- MIT License

