# Unit Converter MCP

Unit conversion utilities that provide precise conversions between different units of measurement.

## 🔧 Tools

| Tool                    | Purpose                                    | Supported Units |
| ----------------------- | ------------------------------------------ | --------------- |
| `convert_temperature`   | Convert temperature between units          | Celsius, Fahrenheit, Kelvin |
| `convert_angle`         | Convert angle between units                | Degrees, Radians, Arcmin, Arcsec, Turns, Gons |
| `convert_length`        | Convert length/distance between units      | Meter, Kilometer, Foot, Inch, Mile, etc. |
| `convert_area`          | Convert area between units                 | Square Meter, Acre, Hectare, Square Foot, etc. |
| `convert_mass`          | Convert mass between units                 | Kilogram, Gram, Pound, Ounce, Ton |
| `convert_volume`        | Convert volume between units               | Liter, Gallon, Cup, Fluid Ounce, etc. |
| `convert_time`          | Convert time between units                 | Seconds, Minutes, Hours, Days, Years, etc. |
| `convert_energy`        | Convert energy between units               | Joule, Kilowatt Hour, Calorie, BTU, etc. |
| `convert_force`         | Convert force between units                | Newton, Pound Force, Kilogram Force, etc. |
| `convert_pressure`      | Convert pressure between units             | Pascal, Bar, PSI, Atmosphere, etc. |
| `convert_power`         | Convert power between units                | Watt, Horsepower, BTU per hour, etc. |
| `convert_speed`         | Convert speed between units                | m/s, mph, km/h, knots, Mach, etc. |
| `convert_computer_data` | Convert computer storage between units     | Bytes, KB, MB, GB, TB, etc. |
| `convert_density`       | Convert density between units              | kg/L, g/cm³, lb/gal, g/L, etc. |
| `list_supported_units`  | List all supported units for each type    | All conversion types |

## 🔧 Examples

Here are some example prompts to get you started:

```text
tell me what unit conversions you can do

convert 0 celcius to F

convert 3.14159 rads to degrees

whats my weight in kg? I'm 205lbs

if I spend 10,000 seconds practicing a skill non-stop, how many days is that?
```


## 🔧 Setup

### Claude Desktop

Add this to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`   
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "unit-converter": {
      "command": "uvx",
      "args": ["unit-converter-mcp"]
    }
  }
}
```

## 📋 Tool Reference

### `convert_temperature`

Convert temperature between Celsius, Fahrenheit, and Kelvin.

**Parameters:**
- `value` (float): Temperature value to convert
- `from_unit` (str): Source unit (celsius, fahrenheit, kelvin)
- `to_unit` (str): Target unit (celsius, fahrenheit, kelvin)

**Example:**
```json
{
  "name": "convert_temperature",
  "arguments": {
    "value": 100,
    "from_unit": "celsius",
    "to_unit": "fahrenheit"
  }
}
```

### `convert_length`

Convert length between various units including metric and imperial systems.

**Parameters:**
- `value` (float): Length value to convert
- `from_unit` (str): Source unit (meter, kilometer, centimeter, millimeter, inch, foot, yard, mile)
- `to_unit` (str): Target unit (meter, kilometer, centimeter, millimeter, inch, foot, yard, mile)

**Example:**
```json
{
  "name": "convert_length",
  "arguments": {
    "value": 1,
    "from_unit": "meter",
    "to_unit": "foot"
  }
}
```

### `convert_mass`

Convert mass between various units including metric, imperial, and specialized units.

**Parameters:**
- `value` (float): Mass value to convert
- `from_unit` (str): Source unit (kilogram, gram, pound, ounce, tonne, carat, stone, etc.)
- `to_unit` (str): Target unit (kilogram, gram, pound, ounce, tonne, carat, stone, etc.)

**Supported Units:**
- Metric: kilogram, gram, milligram, microgram, nanogram, picogram, femtogram, decagram, hectogram, tonne, kilotonne, megatonne
- Imperial: pound, ounce, stone, short ton (US), long ton (UK)
- Precious metals: troy ounce, carat
- Historical: grain

**Example:**
```json
{
  "name": "convert_mass",
  "arguments": {
    "value": 1,
    "from_unit": "kilogram",
    "to_unit": "pound"
  }
}
```

### `convert_volume`

Convert volume between various units including metric and imperial systems.

**Parameters:**
- `value` (float): Volume value to convert
- `from_unit` (str): Source unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce)
- `to_unit` (str): Target unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce)

**Example:**
```json
{
  "name": "convert_volume",
  "arguments": {
    "value": 1,
    "from_unit": "liter",
    "to_unit": "gallon"
  }
}
```

### `convert_time`

Convert time between various units from sub-seconds to millennia.

**Parameters:**
- `value` (float): Time value to convert
- `from_unit` (str): Source unit (seconds, minutes, hours, days, weeks, months, years, etc.)
- `to_unit` (str): Target unit (seconds, minutes, hours, days, weeks, months, years, etc.)

**Example:**
```json
{
  "name": "convert_time",
  "arguments": {
    "value": 1,
    "from_unit": "hours",
    "to_unit": "minutes"
  }
}
```

### `convert_energy`

Convert energy between various units including metric, electrical, heat, nutrition, and particle physics systems.

**Parameters:**
- `value` (float): Energy value to convert
- `from_unit` (str): Source unit (joule, kilowatt hour, calorie, Btu, etc.)
- `to_unit` (str): Target unit (joule, kilowatt hour, calorie, Btu, etc.)

**Supported Units:**
- SI and metric prefixes: joule, kilojoule, megajoule, gigajoule, terajoule, petajoule, exajoule
- Electrical-energy units: watt hour, kilowatt hour, megawatt hour, gigawatt hour, terawatt hour
- Heat / nutrition: Btu, calorie, kilocalorie, therm
- Mechanical & particle-physics units: foot‑pound force, inch‑pound force, erg, electron volt

**Example:**
```json
{
  "name": "convert_energy",
  "arguments": {
    "value": 1,
    "from_unit": "kilowatt hour",
    "to_unit": "joule"
  }
}
```

### `convert_force`

Convert force between various units including metric and imperial systems.

**Parameters:**
- `value` (float): Force value to convert
- `from_unit` (str): Source unit (newtons, pounds force, kilograms force, dynes, kilonewtons, kips, etc.)
- `to_unit` (str): Target unit (newtons, pounds force, kilograms force, dynes, kilonewtons, kips, etc.)

**Supported Units:**
- Metric: newtons, kilonewtons, meganewtons, dynes
- Imperial: pounds force, kips
- Other: kilograms force, tonnes force, long tons force, short tons force

**Example:**
```json
{
  "name": "convert_force",
  "arguments": {
    "value": 100,
    "from_unit": "newtons",
    "to_unit": "pounds force"
  }
}
```

### `convert_density`

Convert density between various units including metric, imperial, and specialized systems.

**Parameters:**
- `value` (float): Density value to convert
- `from_unit` (str): Source unit (kilograms per liter, grams per cubic centimeter, pounds per gallon, etc.)
- `to_unit` (str): Target unit (kilograms per liter, grams per cubic centimeter, pounds per gallon, etc.)

**Supported Units:**
- Grain-based hardness units: grains per gallon (UK), grains per gallon (US), grains per gallon
- Metric staples: grams per cubic centimeter, grams per liter, kilograms per liter, kilograms per cubic meter, milligrams per liter
- Fluid-ounce units: ounces per gallon (UK), ounces per gallon (US), ounces per gallon
- Pound-based units: pounds per cubic foot, pounds per gallon (UK), pounds per gallon (US), pounds per gallon
- Tonne/ton bulk-density units: tonnes per cubic meter, tons per cubic yard (UK), tons per cubic yard (US), tons per cubic yard

**Example:**
```json
{
  "name": "convert_density",
  "arguments": {
    "value": 1,
    "from_unit": "kilograms per liter",
    "to_unit": "grams per cubic centimeter"
  }
}
```

### `list_supported_units`

List all supported units for each conversion type.

**Parameters:** None

**Example:**
```json
{
  "name": "list_supported_units",
  "arguments": {}
}
```

### `convert_angle`

Convert angle between degrees, radians, and other angular units.

**Parameters:**
- `value` (float): Angle value to convert
- `from_unit` (str): Source unit (degrees, radians, arcmin, arcsec, turns, gons)
- `to_unit` (str): Target unit (degrees, radians, arcmin, arcsec, turns, gons)

**Example:**
```json
{
  "name": "convert_angle",
  "arguments": {
    "value": 3.14159,
    "from_unit": "radians",
    "to_unit": "degrees"
  }
}
```

### `convert_area`

Convert area between various units including metric and imperial systems.

**Parameters:**
- `value` (float): Area value to convert
- `from_unit` (str): Source unit (acre, are, hectare, square centimeter, square foot, square inch, square kilometer, square meter, square mile, square millimeter, square yard)
- `to_unit` (str): Target unit (acre, are, hectare, square centimeter, square foot, square inch, square kilometer, square meter, square mile, square millimeter, square yard)

**Example:**
```json
{
  "name": "convert_area",
  "arguments": {
    "value": 1,
    "from_unit": "hectare",
    "to_unit": "acre"
  }
}
```

### `convert_computer_data`

Convert computer storage between various units from bits to exabytes.

**Parameters:**
- `value` (float): Computer storage value to convert
- `from_unit` (str): Source unit (bits, bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, exabytes)
- `to_unit` (str): Target unit (bits, bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, exabytes)

**Example:**
```json
{
  "name": "convert_computer_data",
  "arguments": {
    "value": 1,
    "from_unit": "gigabytes",
    "to_unit": "megabytes"
  }
}
```

### `convert_pressure`

Convert pressure between various units including metric, imperial, and specialized systems.

**Parameters:**
- `value` (float): Pressure value to convert
- `from_unit` (str): Source unit (pascal, hectopascal, kilopascal, megapascal, bar, atmosphere, centimeters of water, inches of water, feet of water, meters of water, millimeters of mercury, inches of mercury, kilogram force per square centimeter, newtons per square centimeter, newtons per square millimeter, psi, psf)
- `to_unit` (str): Target unit (pascal, hectopascal, kilopascal, megapascal, bar, atmosphere, centimeters of water, inches of water, feet of water, meters of water, millimeters of mercury, inches of mercury, kilogram force per square centimeter, newtons per square centimeter, newtons per square millimeter, psi, psf)

**Example:**
```json
{
  "name": "convert_pressure",
  "arguments": {
    "value": 1,
    "from_unit": "atmosphere",
    "to_unit": "psi"
  }
}
```

### `convert_power`

Convert power between various units including mechanical, electrical, and thermal systems.

**Parameters:**
- `value` (float): Power value to convert
- `from_unit` (str): Source unit (Btu per hour, foot pound‑force per second, ton of refrigeration, calorie per hour, kilocalorie per hour, horsepower, horsepower (metric), kilogram‑force meter per second, watt, kilowatt, megawatt, gigawatt, terawatt, petawatt)
- `to_unit` (str): Target unit (Btu per hour, foot pound‑force per second, ton of refrigeration, calorie per hour, kilocalorie per hour, horsepower, horsepower (metric), kilogram‑force meter per second, watt, kilowatt, megawatt, gigawatt, terawatt, petawatt)

**Example:**
```json
{
  "name": "convert_power",
  "arguments": {
    "value": 1,
    "from_unit": "horsepower",
    "to_unit": "kilowatt"
  }
}
```

### `convert_speed`

Convert speed between various units including metric, imperial, and specialized systems.

**Parameters:**
- `value` (float): Speed value to convert
- `from_unit` (str): Source unit (centimeters per minute, centimeters per second, feet per hour, feet per minute, feet per second, inches per minute, inches per second, kilometers per hour, kilometers per second, knots, Mach (ISA sea level), speed of sound, meters per hour, meters per minute, meters per second, miles per hour, miles per minute, miles per second, yards per hour, yards per minute, yards per second, speed of light)
- `to_unit` (str): Target unit (centimeters per minute, centimeters per second, feet per hour, feet per minute, feet per second, inches per minute, inches per second, kilometers per hour, kilometers per second, knots, Mach (ISA sea level), speed of sound, meters per hour, meters per minute, meters per second, miles per hour, miles per minute, miles per second, yards per hour, yards per minute, yards per second, speed of light)

**Example:**
```json
{
  "name": "convert_speed",
  "arguments": {
    "value": 60,
    "from_unit": "miles per hour",
    "to_unit": "meters per second"
  }
}
```

## 🛠️ Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/zazencodes/unit-converter-mcp
cd unit-converter-mcp

# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Run linting
uv run ruff check --fix
uv run ruff format

# Type checking
uv run mypy src/
```

### MCP Client Config

```json
{
  "mcpServers": {
    "unit-converter-dev": {
      "command": "uv",
      "args": [
        "--directory",
        "<path_to_your_repo>/unit-converter-mcp",
        "run",
        "unit-converter-mcp"
      ]
    }
  }
}
```

**Note:** Replace `<path_to_your_repo>/unit-converter-mcp` with the absolute path to your cloned repository.

### Building

```bash
# Build package
uv build

# Test installation
uv run --with dist/*.whl unit-converter-mcp
```

### Release Checklist

1.  **Update Version:**
    - Increment the `version` number in `pyproject.toml` and `src/__init__.py`.

2.  **Update Changelog:**
    - Add a new entry in `CHANGELOG.md` for the release.
        - Draft notes with coding agent using `git diff` context.

        ```
        Update the @CHANGELOG.md for the latest release.
        List all significant changes, bug fixes, and new features.
        Here's the git diff:
        [GIT_DIFF]
        ```
        
    - Commit along with any other pending changes.

3.  **Create GitHub Release:**
    - Draft a new release on the GitHub UI.
        - Tag release using UI.
    - The GitHub workflow will automatically build and publish the package to PyPI.

## Testing with MCP Inspector

For exploring and/or developing this server, use the MCP Inspector npm utility:

```bash
# Install MCP Inspector
npm install -g @modelcontextprotocol/inspector

# Run local development server with the inspector
npx @modelcontextprotocol/inspector uv run unit-converter-mcp

# Run PyPI production server with the inspector
npx @modelcontextprotocol/inspector uvx unit-converter-mcp
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

