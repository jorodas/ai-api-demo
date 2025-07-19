from fastapi import FastAPI
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/ai-answer/")
async def ai_answer(question: str):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=100
    )
    return {"answer": response.choices[0].text.strip()}
