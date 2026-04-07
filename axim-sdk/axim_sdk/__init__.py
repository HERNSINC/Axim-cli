import glob
import importlib.util
import os
import sys

version = f"{sys.version_info[0]}{sys.version_info[1]}"
package_root = os.path.dirname(__file__)

supported_dirs = {
    os.path.basename(path): path
    for path in glob.glob(os.path.join(package_root, "py[0-9][0-9][0-9]"))
}

version_dir = supported_dirs.get(f"py{version}")
if not version_dir:
    supported_versions = ", ".join(sorted(v[2:] for v in supported_dirs.keys()))
    raise ImportError(
        f"Unsupported Python version {version}. Supported versions: {supported_versions}"
    )

inner_pkg_path = os.path.join(version_dir, "axim_sdk")
if inner_pkg_path not in __path__:
    __path__.append(inner_pkg_path)

if version_dir not in sys.path:
    sys.path.insert(0, version_dir)

spec = importlib.util.find_spec("axim_sdk", [version_dir])
if spec is None:
    raise ImportError(f"Could not find version-specific axim_sdk package in {version_dir}")

sdk_name = "__axim_sdk_version__"
if sdk_name in sys.modules:
    sdk = sys.modules[sdk_name]
else:
    sdk = importlib.util.module_from_spec(spec)
    sys.modules[sdk_name] = sdk
    spec.loader.exec_module(sdk)

for attr in dir(sdk):
    if not attr.startswith("_"):
        globals()[attr] = getattr(sdk, attr)
if hasattr(sdk, "__all__"):
    __all__ = sdk.__all__
