
import openai
import zipfile
import os

# ========== USER CONFIGURATION ==========
OPENAI_API_KEY = "your-api-key"  # <-- Replace with your OpenAI API key
EXPORT_ZIP_PATH = "../exports.zip"  # Path to your zipped export directory
MODEL = "gpt-4-1106-preview"
# ========================================

openai.api_key = OPENAI_API_KEY

# Step 1: Upload zip file to OpenAI (requires access to tools/assistants API)
with open(EXPORT_ZIP_PATH, "rb") as f:
    file_response = openai.files.create(file=f, purpose="assistants")

print("Uploaded file ID:", file_response.id)

# Step 2: Send a message to ChatGPT with the file ID and request instructions
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Please generate DO-178C documentation from this zipped Simulink export. Include RTM, SVR, SECI, SAS, and any other relevant artifacts."}
    ],
    tools=[{"type": "file", "id": file_response.id}]
)

# Step 3: Print the response
print("AI Response:")
print(response.choices[0].message["content"])
