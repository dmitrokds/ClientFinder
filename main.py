import traceback

from google import genai
from google.genai import types


async def main():
    model = "gemini-3-flash-preview"
    client = genai.Client(
        api_key="AIzaSyCVPSnbg8qyFdXmUbaBICV7xxnKA1EcPk4",
    )

    agent = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=await gemini.schema.formating(eval(payload.response_schema)),
        system_instruction=[types.Part.from_text(text=prompt) for prompt in payload.prompts]
    )
    
    error = None
    for _ in range(10):
        try:
            res = client.models.generate_content(
                model=model,
                contents="",
                config=agent,
            )
            break
        except Exception as e:
            error = traceback.format_exc()
            
            
    print(error)