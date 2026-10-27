from chattonpy import generate
import os

response = generate("Tell me a joke", os.environ.get("GEMINI_API_KEY"), thinking_level="LOW", model="gemma-4-26b-a4b-it")
print(response)