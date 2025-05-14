
# Step 2: Use Groq to analyze the extracted text
from groq import Groq

client = Groq(api_key="your_groq_api_key")

response = client.chat.completions.create(
    model="llama3-8b-8192",  # supported Groq model
    messages=[
        {"role": "system", "content": "You are a medical assistant."},
        {"role": "user", "content": f"Analyze this OCR text:\n{ocr_result}"}
    ]
)

print(response.choices[0].message.content)



import base64
import requests

# Load and encode the image
with open("path_to_your_image.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the payload
payload = {
    "model": "llava-v1.5-7b-4096-preview",
    "messages": [
        {
            "role": "user",
            "content": "Please extract all text from this image."
        }
    ],
    "images": [encoded_image]
}

# Set your API key
headers = {
    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
}

# Send the request
response = requests.post("https://api.groq.com/v1/chat/completions", headers=headers, json=payload)

# Output the result
print(response.json())






import os
import base64
from groq import Groq

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Path to your image file
image_path = "path_to_your_image.jpg"

# Read and encode the image in base64
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the message for OCR
messages = [
    {
        "role": "user",
        "content": "Please extract all text from this image."
    }
]

# Send the request to the Groq API
response = client.chat.completions.create(
    model="llava-v1.5-7b-4096-preview",  # Replace with the appropriate vision model ID
    messages=messages,
    images=[encoded_image]
)

# Output the OCR result
print(response.choices[0].message.content)
