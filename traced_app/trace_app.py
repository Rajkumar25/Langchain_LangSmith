

import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


print("LangSmith is connected!")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatOpenAI(model="gpt-4o-mini")
prompts = [
        "Explain what a database index is in simple terms.",
        "Write a short Python function to calculate factorial recursively.",
        "Explain why LangSmith tracing is useful when debugging an LLM application."
    ]
for i, prompt in enumerate(prompts, start=1):
        print(f"\n{'=' * 60}")
        print(f"PROMPT {i}")
        print(f"{'=' * 60}")
        print(prompt)

        response = model.invoke(prompt)

        print(f"\nANSWER {i}")
        print(f"{'-' * 60}")
        print(response.content)