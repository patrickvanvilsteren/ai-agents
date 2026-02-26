import asyncio
import os

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    client= OpenAIChatClient(env_file_path=".env")
    agent = Agent(
        client=client,
        instructions="You are a helpful assistant which has knowledge about military assets like tanks, planes, ships, etc. You can answer questions about these assets and provide information on their capabilities, specifications, and history."
    )
    result = await agent.run("What are the capabilities of the M1 Abrams tank?")
    print(result)

asyncio.run(main())