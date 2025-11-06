# pip install agent-framework
from dotenv import load_dotenv
import asyncio
import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from typing import Annotated
from pydantic import Field
import litellm

# set env variable
litellm.use_litellm_proxy = True
load_dotenv()

api_base = os.getenv("LITELLM_ROXY_URL")
api_key = os.getenv("LITELLM_MASTER_KEY")

# Tool definition
def get_weather(
    city: Annotated[str, Field(description="The location to get weather for")]
) -> str:
    city_normalized = city.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": "The weather in New York is sunny with a temperature of 25°C.",
        "london": "It's cloudy in London with a temperature of 15°C.",
        "tokyo": "Tokyo is experiencing light rain and a temperature of 18°C.",
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return f"The weather in {city} is sunny with a temperature of 20°C."

# Create agent using OpenAIClient
agent = ChatAgent(
    chat_client=OpenAIChatClient(model_id="sap/gpt-4o",
                                 api_key=api_key,
                                 base_url=api_base,),
    instructions="You are a helpful weather assistant. "
                "When the user asks for the weather in a specific city, "
                "use the 'get_weather' tool to find the information. "
                "If the tool returns an error, inform the user politely. "
                "If the tool is successful, write a couple sentences for "
                "TV weather report in the city, that will be include small jok",
    name="litellm_agent",
    tools=[get_weather],
)

async def tools_example():
    result = await agent.run("What's the weather like in Tokyo?")
    print(result.text)

asyncio.run(tools_example())