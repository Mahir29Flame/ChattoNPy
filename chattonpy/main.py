# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import sys
from google import genai
from google.genai import types
from typing import List

__version__ = "1.2.7"

def generate(text: str, api_key: str, history: list | None = None):
    if history is None:
        history = []
    client = genai.Client(
        api_key=api_key,
    )

    model = "gemini-3.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=text),
            ],
        ),
    ]
    tools = [
        types.Tool(code_execution=types.ToolCodeExecution()),
        types.Tool(url_context=types.UrlContext()),
    ]
    generate_content_config = types.GenerateContentConfig(
        system_instruction=f"You are a helpful assistant.\nHistory:\n{''.join(history)}",
        thinking_config=types.ThinkingConfig(
            thinking_level="MEDIUM",
        ),
        audio_transcription_config=types.AudioTranscriptionConfig(
        ),
        tools=tools,
    )

    full_response = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response.append(chunk.text)
    print()

    return "".join(full_response)

ChattoNPY = generate

def cli():
    """CLI entrypoint for ChattoNPy."""
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"ChattoNPy v{__version__}")
        return

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Set it with:  $env:GEMINI_API_KEY = 'your-key-here'")
        sys.exit(1)

    history = []
    while True:
        try:
            user_input = input("You> ")
            if user_input.strip() in ("/quit()"):
                break
            print("\nAI> ")
            output = generate(user_input, api_key, history)
            history.append(f"\nUser: {user_input}\nAI: {output}")
            print()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    cli()
