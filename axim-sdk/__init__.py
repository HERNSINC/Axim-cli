import sys
import os

# Version-aware package loading for Axim SDK
version = f"{sys.version_info[0]}{sys.version_info[1]}"

# Map Python versions to package directories
version_map = {
    "312": "py312",
    "313": "py313",
    "314": "py314"
}

version_dir = version_map.get(version)
if version_dir:
    package_path = os.path.join(os.path.dirname(__file__), version_dir)
    if os.path.isdir(package_path):
        # Add the version-specific package to Python path
        if package_path not in sys.path:
            sys.path.insert(0, package_path)
        # Import the version-specific package
        import axim_sdk
        # Copy all attributes to this module
        for attr in dir(axim_sdk):
            if not attr.startswith('_'):
                globals()[attr] = getattr(axim_sdk, attr)
        # Copy __all__ if it exists
        if hasattr(axim_sdk, '__all__'):
            __all__ = axim_sdk.__all__
    else:
        raise ImportError(f"Version-specific package not found for Python {version}: {package_path}")
else:
    raise ImportError(f"Unsupported Python version {version}. Supported versions: 3.12, 3.13, 3.14")