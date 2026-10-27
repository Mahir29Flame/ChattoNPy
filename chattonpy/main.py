# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import argparse
import sys
from google import genai
from google.genai import types
from typing import List

__version__ = "1.5.1"

def generate(text: str, api_key: str, model: str = "gemini-3.5-flash-lite", thinking_level: str = "MEDIUM", history: list | None = None):
    if history is None:
        history = []
    client = genai.Client(
        api_key=api_key,
    )

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
        types.Tool(url_context=types.UrlContext()) if "gemini" in model else types.Tool(),
    ]
    if "gemini" in model:
        thinking_config = types.ThinkingConfig(
            thinking_level=thinking_level,
        )
    else:
        thinking_config = None
    generate_content_config = types.GenerateContentConfig(
        system_instruction=f"You are a helpful assistant. Your name is Chatty.\nHistory:\n{''.join(history)}",
        thinking_config=thinking_config,
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

def cli(*args,**kwargs):
    """CLI entrypoint for ChattoNPy."""
    parser = argparse.ArgumentParser(
        prog="ChattoNPy",
        description="Ask and Chat with Chatty — a terminal AI assistant powered by Gemini.",
    )

    model_choices = [
        "gemini-3.5-flash-lite [500 Req. per day]",
        "gemini-3.1-flash-lite [500 Req. per day]",
        "gemma-4-26b-a4b-it [14.4K Req. per day]",
        "gemma-4-31b-it [14.4K Req. per day]",
        "gemini-2.5-flash [20 Req. per day]",
        "gemini-2.5-flash-lite [20 Req. per day]",
        "gemini-3-flash [20 Req. per day]",
        "gemini-3.6-flash [20 Req. per day]",
        "gemini-3.8-flash [20 Req. per day]",
    ]
    model_short_map = {m.split(" ")[0]: m for m in model_choices}

    parser.add_argument(
        "--model",
        default="gemini-3.5-flash-lite",
        choices=model_choices + list(model_short_map.keys()),
        help="The model to use (default: gemini-3.5-flash-lite).",
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"ChattoNPy v{__version__}",
    )

    parser.add_argument(
        "--models", "--list-models", "--list",
        action="store_true",
        dest="list_models",
        help="List all available models with rate limits.",
    )

    parser.add_argument(
        "--thinking" "-t",
        default="AUTO",
        choices=["LOW", "MEDIUM", "HIGH"],
        help="The thinking level to use (default: LOW)."
    )

    args = parser.parse_args()

    if args.list_models:
        print("\nAvailable Models:")
        print(
        """
        gemini-3.5-flash-lite [500 Req. per day] (Default) \n
        gemini-3.1-flash-lite [500 Req. per day] \n
        gemma-4-26b-a4b-it [14.4K Req. per day] \n
        gemma-4-31b-it [14.4K Req. per day] \n
        gemini-2.5-flash [20 Req. per day] \n
        gemini-2.5-flash-lite [20 Req. per day] \n
        gemini-3-flash [20 Req. per day] \n
        gemini-3.6-flash [20 Req. per day] \n
        gemini-3.8-flash [20 Req. per day] \n

        usage: ChattoNPy --model [model-name]
        """)
        return
        
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Set it with:  $env:GEMINI_API_KEY = 'your-key-here'")
        sys.exit(1)

    model = args.model
    if model in model_short_map:
        model = model_short_map[model]
    elif model in list(model_short_map.keys()) or model.split(" ")[0] in model_short_map:
        # try to extract short form
        short = model.split(" ")[0]
        if short in model_short_map:
            model = model_short_map[short]
    else:
        # if someone passes just short form without space, check
        for k, v in model_short_map.items():
            if model == k:
                model = v
                break
    # extract just the model name part before space for API
    model_name = model.split(" ")[0]

    thinking_level = args.thinking_t
    if thinking_level == "AUTO":
        thinking_level = "MEDIUM"

    history = []
    while True:
        try:
            user_input = input("\n 𝒴𝑜𝓊> ")
            if user_input.strip() in ("/quit()"):
                break
            print("\n 𝒜 𝐼⤵ ")
            output = generate(user_input, api_key, model_name, thinking_level, history)
            history.append(f"\nUser: {user_input}\nAI: {output}")
            print()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    cli()
