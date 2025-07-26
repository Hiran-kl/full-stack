pip install fastapi uvicorn

import openai
openai.api_key  = "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"
def get_llm_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
  
 from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class PromptRequest(BaseModel):
    prompt: str
@app.post("/generate")
async def generate_response(request: PromptRequest):
    try:
        response = get_llm_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=8000)  
