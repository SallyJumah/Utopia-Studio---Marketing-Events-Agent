# Utopia Studio · Marketing & Events Agent

Takes a raw Granola meeting transcript and outputs a LinkedIn post, personalised follow-up email, and press angle sentence — ready to use within the hour.

## How to run

1. Install dependencies:
   pip install requests python-dotenv

2. Create a .env file:
   OPENROUTER_API_KEY=your_key_here

3. Paste your transcript into transcript.txt

4. Run:
   python main.py

5. Output is printed to terminal and saved to output.json

## Prompts used

System prompt: Instructs the model to act as Utopia Studio's Marketing & Events agent. Enforces declarative voice, no hedging, no invented statistics, and maps each output to the LAUNCH framework (Lead = LinkedIn, Nurture = email, Amplify = press angle).

User prompt: Passes the raw transcript and requests a strict JSON structure with four fields: linkedin_post, follow_up_email, press_angle, launch_stage.

## Tools and APIs

- OpenRouter API (openrouter/free) — LLM inference
- python-dotenv — environment variable management

## Output format

{
  "linkedin_post": "...",
  "follow_up_email": "...",
  "press_angle": "...",
  "launch_stage": {
    "linkedin_post": "Lead",
    "follow_up_email": "Nurture",
    "press_angle": "Amplify"
  }
}

Structured JSON so a downstream agent (Slack poster, Linear issue creator, etc.) can pick it up without a human in the middle.
