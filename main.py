import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("ERROR: OPENROUTER_API_KEY not found in .env")
    exit()

with open("transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

system_prompt = """
You are the Marketing & Events AI Agent for Utopia Studio.

Your task:
- Read a meeting transcript
- Generate:
  1. LinkedIn post
  2. Personalized follow-up email
  3. Press angle sentence

Voice:
- Declarative
- Opinionated
- Specific
- No hedging
- No corporate fluff

Rules:
- Do not invent statistics or market numbers
- Only use information supported by the transcript

LAUNCH framework:
- LinkedIn post = Lead
- Follow-up email = Nurture
- Press angle = Amplify

Return raw JSON only.
"""

user_prompt = f"""
Transcript:

{transcript}

Return this JSON structure:

{{
  "linkedin_post": "...",
  "follow_up_email": "...",
  "press_angle": "...",
  "launch_stage": {{
    "linkedin_post": "Lead",
    "follow_up_email": "Nurture",
    "press_angle": "Amplify"
  }}
}}
"""

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/free",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7
    },
    timeout=60
)

data = response.json()

if "choices" not in data:
    print("API Error:")
    print(data)
    exit()

output_text = data["choices"][0]["message"]["content"]
output_text = output_text.replace("```json", "").replace("```", "").strip()

start = output_text.find('{')
end = output_text.rfind('}') + 1
output_text = output_text[start:end]

print("\nGenerated Output:\n")
print(output_text)

try:
    parsed_json = json.loads(output_text)

    with open("output.json", "w", encoding="utf-8") as outfile:
        json.dump(parsed_json, outfile, indent=2)

    print("\nOutput saved to output.json")

except Exception as e:
    print("\nCould not save valid JSON.")
    print(e)