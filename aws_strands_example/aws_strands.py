from strands.models.litellm import LiteLLMModel
from strands import Agent
from strands.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool
def get_weather(city: str):
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


agent = Agent(
    system_prompt="You are a helpful weather assistant. "
            "When the user asks about a specific city, "
            "use the 'get_weather' tool to find the weather information. "
            "Provide the TV weather report in two sentences including a small joke.",
    model=LiteLLMModel(model_id="sap/gpt-5"),
    tools=[get_weather],
)


response = agent("london")
print(response)
