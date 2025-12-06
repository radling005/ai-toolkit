import os
import anthropic

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        return

    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": "Hello, Claude! Tell me a fun fact about the ocean."}
            ]
        )
        print(message.content[0].text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
