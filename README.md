# Axim code

A high-performance agentic CLI and web-based terminal rewritten in Python.

## Structure

- `axim-sdk` (Python): High-level agent and tool logic.
- `web` (Python/FastAPI): Web interface for the agent.

## How to use

### CLI
1.  Navigate to `axim-sdk`.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Run the CLI: `python run_cli.py`.
    *   **Note**: On first run, you will be prompted to enter your **Mistral API Key**. This will be saved to a local `.env` file for future sessions.

### Web
1.  Navigate to `web`.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Create a `.env` file in the `web` folder and add `MISTRAL_API_KEY=your_key_here`.
4.  Run the server: `python main.py`.

## Protection and Compatibility
This repository contains a protected version of Axim (Obfuscated using PyArmor). 
The source code is encrypted to prevent reverse engineering while maintaining full functionality.

- **Cross-Platform Support**: The current build supports both **Windows (x64)** and **macOS (Intel/Apple Silicon via Rosetta)**.
- **Privacy**: The core logic is protected and bound to HERNS INC / GRRN licenses.

## Progress

The following tools have been ported from the original project:
- `BashTool`: Stateful bash command execution with security checks.
- `Agent`: Core orchestrator with history management and persistence.
- `ShellProvider`: Flexible shell backend supporting both Rust and native Python.
