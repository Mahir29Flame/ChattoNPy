from chattonpy import generate
import os

response = generate("Tell me a joke", os.environ.get("GEMINI_API_KEY"))
print(response)