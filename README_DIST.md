# Axim-Git Version Selection

Because PyArmor rigidly ties its secure C-extensions to the exact Python ABI (Application Binary Interface), it is impossible to distribute one single folder that works across Python 3.10, 3.11, and 3.12 without complex external runtime loaders that often trigger `dlopen` failures on newer macOS versions like Tahoe.

To guarantee this works flawlessly on your system regardless of your OS (macOS Intel/ARM, Windows, Linux) and Python version, **this repository now contains distinct pre-compiled distributions**.

## How to use:

1. Identify your Python version (`python3 --version`).
2. Use the folder corresponding to your version:
   - Python 3.10 -> use the `py310` / `web310` folders.
   - Python 3.11 -> use the `py311` / `web311` folders.
   - Python 3.12 -> use the `py312` / `web312` folders.

Each of these folders contains the fully cross-platform `pyarmor_runtime_000000` extensions tailored specifically for that Python version's C-API.

## Example Installation (Python 3.11)
```bash
# For the SDK:
cd axim-sdk/py311
pip install -e .  # (Ensure your pyproject.toml is at this level or copy the source out)

# For the Web backend:
cd web/web311
python main.py
```
