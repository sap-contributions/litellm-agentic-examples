from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.litellm import LiteLLMProvider
from dotenv import load_dotenv
import os
import litellm

litellm.use_litellm_proxy = True

load_dotenv()
api_base = os.getenv("LITELLM_ROXY_URL")
api_key = os.getenv("LITELLM_MASTER_KEY")
model = OpenAIChatModel(
    "sap/gpt-5",
    provider=LiteLLMProvider(
        api_base=api_base,
        api_key=api_key,
    ),
)
agent = Agent(
    model=model,
    system_prompt="You are a helpful weather assistant. "
    "When the user send you asks a specific city, "
    "use the 'get_weather' tool to find the information about the weather. "
    "Aser with TV weather report in two sentences, include small jok",
)


@agent.tool
def get_weather(city: RunContext[str]) -> str:
    """Mock function"""
    city_normalized = city.prompt.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": "The weather in New York is sunny with a temperature of 25°C.",
        "london": "It's cloudy in London with a temperature of 15°C.",
        "tokyo": "Tokyo is experiencing light rain and a temperature of 18°C.",
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return f"The weather in {city} is sunny with a temperature of 20°C."


result = agent.run_sync("London")
print(result.output)
