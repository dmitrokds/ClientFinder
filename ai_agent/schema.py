from google import genai
from google.genai import types

async def creating(schema: str):
    schema = eval(schema.replace("    ", "").replace("\n", ""))
    
    async def to_schema(el):
        basic_types = {
            str: types.Type.STRING,
            int: types.Type.INTEGER,
            bool: types.Type.BOOLEAN,
            float: types.Type.NUMBER
        }
        
        if isinstance(el, dict):
            return types.Schema(
                type = types.Type.OBJECT,
                required = [sub_key[:-2] for sub_key in el.keys() if sub_key.endswith("**")],
                properties = {
                    sub_key[:-2] if sub_key.endswith("**") else sub_key: await to_schema(sub_schema)
                    for sub_key, sub_schema in el.items()
                }
            )
            
        if isinstance(el, list):
            if len(el) != 1:
                return None
            
            return types.Schema(
                type = types.Type.ARRAY,
                items = await to_schema(el[0])
            )
        
            
            
        if el in basic_types:
            return types.Schema(
                type = basic_types.get(el),
            )
        
    
    return await to_schema(schema)