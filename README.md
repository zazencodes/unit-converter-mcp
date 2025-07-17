# Unit Converter MCP

Unit conversion utilities that provide precise conversions between different units of measurement.

## 🔧 Tools

| Tool                    | Purpose                                    | Supported Units |
| ----------------------- | ------------------------------------------ | --------------- |
| `convert_temperature`   | Convert temperature between units          | Celsius, Fahrenheit, Kelvin |
| `convert_length`        | Convert length/distance between units      | Meter, Kilometer, Foot, Inch, Mile, etc. |
| `convert_weight`        | Convert weight/mass between units          | Kilogram, Gram, Pound, Ounce, Ton |
| `convert_volume`        | Convert volume between units               | Liter, Gallon, Cup, Fluid Ounce, etc. |
| `list_supported_units`  | List all supported units for each type    | All conversion types |

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

### `convert_weight`

Convert weight/mass between various units.

**Parameters:**
- `value` (float): Weight value to convert
- `from_unit` (str): Source unit (kilogram, gram, pound, ounce, ton)
- `to_unit` (str): Target unit (kilogram, gram, pound, ounce, ton)

**Example:**
```json
{
  "name": "convert_weight",
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

## 📚 Links

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Python unit conversion libraries](https://docs.python.org/3/library/)
