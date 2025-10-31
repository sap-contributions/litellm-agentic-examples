from __future__ import annotations
# pip install "openai-agents[litellm]"
import asyncio
import json
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
load_dotenv()
# use function like this to build json string from your sap credentials, or set it in such vay in .env file
def build_aicore_config_json():
    config = {
        "AICORE_AUTH_URL": os.getenv("AICORE_AUTH_URL", ""),
        "AICORE_BASE_URL_ID": os.getenv("AICORE_BASE_URL_ID", ""),
        "AICORE_BASE_URL": os.getenv("AICORE_BASE_URL", ""),
        "AICORE_CLIENT_ID": os.getenv("AICORE_CLIENT_ID", ""),
        "AICORE_CLIENT_SECRET": os.getenv("AICORE_CLIENT_SECRET", ""),
        "AICORE_RESOURCE_GROUP": os.getenv("AICORE_RESOURCE_GROUP", "")
    }

    # Преобразуем словарь в красивую JSON-строку
    json_str = json.dumps(config, indent=2)
    return json_str

@function_tool
def get_weather(city: str):
    city_normalized = (city.lower().replace(" ", ""))

    mock_weather_db = {
        "newyork": "The weather in New York is sunny with a temperature of 25°C.",
        "london": "It's cloudy in London with a temperature of 15°C.",
        "tokyo": "Tokyo is experiencing light rain and a temperature of 18°C.",
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return f"The weather in {city} is sunny with a temperature of 20°C."


async def main(model: str, city: str = "Tokyo"):
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful weather assistant. "
                "When the user send you asks a specific city, "
                "use the 'get_weather' tool to find the information about the weather. "
                "Aser with TV weather report in two sentences, include small jok",
        model=LitellmModel(model=model, api_key=build_aicore_config_json()),
        tools=[get_weather],
    )

    result = await Runner.run(agent, f"What's the weather in {city}?")
    print(result.final_output)


if __name__ == "__main__":
    city = input("Input city: ")
    asyncio.run(main(model='sap/gpt-4.1', city=city))