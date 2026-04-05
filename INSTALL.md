# Installing Axim (GRRN / HERNS INC)

Axim is a high-performance agentic terminal and prediction engine. This version is protected and branded for official GRRN use.

## Prerequisites

- **Python 3.10+**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
- **Mistral API Key**: You will need a personal API key from [Mistral AI](https://console.mistral.ai/).
- **Ollama (Optional for Offline)**: If you want to use the local fallback (Gemma), install [Ollama](https://ollama.com/).

---

## Installation on Windows

1. **Download the Repository**: Download the Axim-Git folder to your PC.
2. **Open Terminal**: Open `PowerShell` or `Command Prompt` and navigate to the folder:
   ```powershell
   cd Axim-Git/axim-sdk
   ```
3. **Set up Virtual Environment**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
4. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
5. **Run Axim**:
   ```powershell
   python run_cli.py
   ```
6. **Setup**: On first run, paste your **Mistral API Key** when prompted. It will be saved locally.

---

## Installation on macOS

1. **Open Terminal**: Navigate to the Axim-Git folder:
   ```bash
   cd Axim-Git/axim-sdk
   ```
2. **Set up Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Axim**:
   ```bash
   python3 run_cli.py
   ```
5. **Setup**: Follow the on-screen prompt to enter your **Mistral API Key**.

---

## Offline / Local Fallback Mode
If you don't have a Mistral key or prefer to run locally:
1. Install **Ollama**.
2. Run `ollama run gemma2:2b`.
3. In the Axim terminal, type: `switch to gemma`.

---

## Licensing & Terms
This software is the proprietary property of **HERNS INC / GRRN**. 
- **Website**: [https://www.grrn.io](https://www.grrn.io)
- **Support**: [support.team@grrn.io](mailto:support.team@grrn.io)

*Reverse engineering, unauthorized redistribution, or commercial use is strictly prohibited under the included LICENSE.*
