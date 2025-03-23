"""
Step 2:
Text Generation using Gemini API
generate API key from: https://ai.google.dev/gemini-api/docs/api-key
"""

import google.generativeai as genai

# Configure the Gemini API with your API key.
genai.configure(api_key="AIzaSyDcx39dpx5qe4OKSe6L7hi7W7s9bb_KVb0")


def gemini_api(text):
    # Initialize a genAI model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # generate a response based on the input text.
    response = model.generate_content(text)

    print(response.text)


# -------------MAIN----------------

text = "2+2= what"
gemini_api(text)
