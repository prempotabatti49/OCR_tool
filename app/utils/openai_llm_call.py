from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


def call_llm_openai(messages):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

