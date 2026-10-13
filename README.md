# Security-Agents-Project

This code will prompt Gemini using model gemini-3.5-flash-lite with 3 questions, prepended with system instructions telling it not to go too in-depth 

Instructions to run the code:

Create the project directory and navigate into it.

Create the .venv virtual environment (python -m venv .venv) and activate it (.venv/bin/activate)

Install the google-genai package using "python -m pip install --upgrade google-genai"

Obtain an API key from Google AI Studio and keep it private.

Set the GEMINI_API_KEY environment variable in your terminal using "export GEMINI_API_KEY="YOUR_API_KEY""

Create main.py in your project directory.

Add the system instruction, three prompts, Gemini client, and response-printing loop.

Select a supported Gemini model ID.

Run "python main.py" and verify the responses.
