import cache
import traceback

import json


async def init(name: str, text: str):
    if name not in cache.agents:
        return 405, "Agent wasnt find"
    
    error = None
    for _ in range(10):
        try:
            res = cache.agents[name]["client"].models.generate_content(
                model=cache.agents[name]["model"],
                contents=text,
                config=cache.agents[name]["agent"],
            )
            return 200, json.loads(res.text)
        
        
        except Exception as e:
            error = traceback.format_exc()
            
            
    return 500, error