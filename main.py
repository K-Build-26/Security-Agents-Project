from google import genai
from google.genai import types

# Configure Gemini API
client = genai.Client()

# Tell Gemini how to respond
SYSTEM_INSTRUCTION = """
I will be asking you 3 prompts.
Keep your answers concise and straightforward.
Do not go into too much detail.
Focus on the key information.
"""

# The three prompts
PROMPTS = [
    "Prompt 1: What is phishing, and how can you recognize a phishing email?",
    """Prompt 2: Is this Python code vulnerable to SQL injection? 
    query = "SELECT * FROM users WHERE username = '" + username + "'""",
    """Prompt 3: Explain what happens when an attacker injects
    ' OR 1=1 -- into a vulnerable SQL query.""",
]

# Use Gemini Flash
MODEL = "gemini-3.5-flash-lite"

def main():
    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=300,
        ),
    )

    for prompt in PROMPTS:
        print(f"\n{prompt}")
        response = chat.send_message(prompt)
        print(f"Gemini: {response.text}")

if __name__ == "__main__":
    main()
