# Axim SDK - Multi-Version Package

This package provides obfuscated Axim SDK binaries compatible with Python 3.12, 3.13, and 3.14.

## Installation

Copy the entire `axim-sdk-multi-version` directory to your project and import it:

```python
import axim_sdk
```

The package automatically detects your Python version and loads the appropriate obfuscated binaries.

## Supported Python Versions

- Python 3.12
- Python 3.13
- Python 3.14

## Structure

```
axim-sdk-multi-version/
├── __init__.py          # Auto-detection loader
├── py312/               # Python 3.12 specific binaries
├── py313/               # Python 3.13 specific binaries
└── py314/               # Python 3.14 specific binaries
```

## Manual Version Selection

If you need to use a specific version, you can import directly:

```python
import sys
sys.path.insert(0, 'py312')  # For Python 3.12
import axim_sdk
```

## Build Process

Each version was built using PyArmor with the corresponding Python version to ensure runtime compatibility.