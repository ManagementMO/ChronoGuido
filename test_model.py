import google.generativeai as genai
import os

# Set your API Key (securely!)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBniRanVvZaWIDND2z7V_GVjdMkE3nMBmA" # Your API KEY here

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use your fine-tuned model ID here
model = genai.GenerativeModel('gemini-1.5-flash') # REPLACE WITH YOUR MODEL ID

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    response = model.generate_content(user_input)
    print("AI:", response.text)