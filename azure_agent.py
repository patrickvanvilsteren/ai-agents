import asyncio
import os

print("API VERSION:", os.getenv("AZURE_OPENAI_API_VERSION"))

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from agent_framework.azure import AzureOpenAIChatClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = AzureOpenAIChatClient(env_file_path=".env", api_version="2024-06-01")
    agent = Agent(client=client, instructions="You are a helpful assistant which has knowledge about military assets like tanks, planes, ships, etc. You can answer questions about these assets and provide information on their capabilities, specifications, and history.")
    print(await agent.run("What are the capabilities of the M1 Abrams tank?"))

asyncio.run(main())