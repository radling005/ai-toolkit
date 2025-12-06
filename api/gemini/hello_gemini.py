import os
import google.generativeai as genai

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    try:
        response = model.generate_content("Hello, Gemini! Tell me a fun fact about space.")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
