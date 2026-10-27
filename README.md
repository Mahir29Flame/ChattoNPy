# ChattoNPy
#### *A simple python CLI chat interface and module for Gemini API*
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/chattonpy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/chattonpy)

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
