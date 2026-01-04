from google import genai
from google.genai import types

import config, cache

import traceback


async def init(
    name: str,
    prompts: list[str], schema: types.Schema, 
    google_search: bool = False,
    thinking_budget: int|None=None, thinking_level: str|None=None,
    model: str = "gemini-3-flash-preview"
) -> int:
    try:
        client = genai.Client(
            api_key=config.GEMINI_TOKEN,
        )    

        agent = types.GenerateContentConfig(
            thinking_config = types.ThinkingConfig(
                thinking_budget=thinking_budget if thinking_budget is not None else None,
                thinking_level=thinking_budget if thinking_level is not None else None
            ) if thinking_budget is not None and thinking_level is not None else None,
            response_mime_type="application/json",
            response_schema=schema,
            system_instruction=[types.Part.from_text(text=prompt) for prompt in prompts],
            tools = [types.Tool(google_search=types.GoogleSearch())] if google_search else None
        )
            
    except:
        return 500, traceback.format_exc()
    
    cache.agents[name] = {
        "client": client,
        "agent": agent,
        "model": model
    }
    
    return 200, name