# ChattoNPy
#### *A simple python CLI chat interface and module for Gemini API*
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/chattonpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/chattonpy)

Table of Contents:

- [ChattoNPy](#chattos-cli-interface)
  - [Features](#features)
  - [Installation](#installation)
    - [Install as a CLI Tool](#install-as-a-cli-tool)
    - [Install as a Module](#install-as-a-module)
  - [Usage](#usage)
    - [As a CLI Tool](#as-a-cli-tool)
    - [As a Module](#as-a-module)
    - [Module Arguments](#module-arguments)
  - [Available Models](#available-models)
  - [Arguments](#arguments)
  - [License](LICENSE)

## Why use ChattoNPy?

- ChattoNPy can make using Google GenAI API in code much simpler as a module.

- ChattoNPy does not require a complex setup.

- ChattoNPy is free to use and contribute.

- ChattoNPy is easy to use in Terminal with a single word to start.

- ChattoNPy is fast, efficient and lightweight.

- ChattoNPy can be ideal for embedded devices because of its untrackably low memory footprint.

- While it's not the prettiest and most feature-rich - I have ambitions for it to reach a place where it will be loved and adored by The Open-Source Community.

## Installation

### Install as a CLI Tool

```bash
pipx install ChattoNPy
```

or via UV:

```bash
uv tool install ChattoNPy
```

### Install as a Module

```bash
pip install ChattoNPy
```

or via UV:

```bash
uv add ChattoNPy
```

## Usage

### CLI 
Set the API key as an environment variable:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

On linux/macOS:
```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

Then run the tool:

```bash
ChattoNPy
```

### Module

```python
from chattonpy import generate
import os

response = generate("Tell me a joke", os.environ.get("GEMINI_API_KEY"), thinking_level="LOW", model="gemma-4-26b-a4b-it")
print(response)
```

All input arguments in one call:

```python
response = generate("Tell me a joke", "YOUR_API_KEY", "LOW", model="gemma-4-26b-a4b-it", history=[])
```

## Available Models

- Gemini:
  - gemini-3.5-flash-lite   -  [500 Req. per day] (Default)
  - gemini-3.1-flash-lite   -  [500 Req. per day]
  - gemini-2.5-flash        -  [20 Req. per day]
  - gemini-2.5-flash-lite   -  [20 Req. per day]
  - gemini-3-flash          -  [20 Req. per day]
  - gemini-3.6-flash        -  [20 Req. per day]
  - gemini-3.8-flash        -  [20 Req. per day]
 
- Gemma:
  - gemma-4-26b-a4b-it      -  [14.4K Req. per day]
  - gemma-4-31b-it          -  [14.4K Req. per day]

## Arguments


- `--version` : Show the version of the tool.
- `--help` : Show the help message.
- `--model [model-name]` : The model to use (default: gemini-3.5-flash-lite).
- `--thinking [thinking-level]` : The thinking level to use (default: MEDIUM).
- `--list-models` : List all available models with rate limits.