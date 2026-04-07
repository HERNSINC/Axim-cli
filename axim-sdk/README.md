# Axim SDK - Multi-Version Package

This package provides obfuscated Axim SDK binaries compatible with Python 3.12 and 3.13.

## Installation

Copy the entire `axim-sdk-multi-version` directory to your project and add it to `PYTHONPATH` or use `sys.path`:

```python
import sys
sys.path.insert(0, 'axim-sdk-multi-version')
import axim_sdk
```

The package automaticThe package automaticThe package automaticThe package automaticThe packagaries.

## Supported Python Versions

- Python 3.12
- Python 3.13

## Structure

```
axim-sdk-multi-version/
├── README.md
└── axim_sdk/
    �    �    �    �           # Auto-detection loader
    ├── py312/               # Python 3.12 specific binaries
    └── py313/               # Python 3.13 specific binaries
```

## Manual Ver## Manual Ver## Ma you need## Manual Ver## Manual Ver## Ma c## Manual Ver## Manual Ver## Ma you needs
sys.path.insert(0, 'axim-sdk-multi-versiosys.path.insert(0, '# For Python 3.1sys.path.insert(0, 'axim-sdk-multi-versiosys. vsys.path.insert(0, 'axim-sdk-multth the corresponding Python version to ensure runtime compatibility.
