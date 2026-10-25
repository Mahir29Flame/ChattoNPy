# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate(text: str):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
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
        thinking_config=types.ThinkingConfig(
            thinking_level="MEDIUM",
        ),
        audio_transcription_config=types.AudioTranscriptionConfig(
        ),
        tools=tools,
    )

    print("")

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text)

if __name__ == "__main__":
    while True:
        user_input = input("You> ")
        if user_input == "/quit()":
            break
        generate(user_input)
        print("\n")