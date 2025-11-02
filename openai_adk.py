from __future__ import annotations
# pip install "openai-agents[litellm]"
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
load_dotenv()

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
                "When the user asks you about a specific city, "
                "use the 'get_weather' tool to find the information about the weather. "
                "Answer with a TV weather report in two sentences, including a small joke.",
        model=LitellmModel(model=model),
        tools=[get_weather],
    )

    result = await Runner.run(agent, f"What's the weather in {city}?")
    print(result.final_output)


if __name__ == "__main__":
    city = input("Input city: ")
    asyncio.run(main(model='sap/gpt-4.1', city=city))