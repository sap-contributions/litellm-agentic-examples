# pip install "smolagents[toolkit]"
from dotenv import load_dotenv
from smolagents import LiteLLMModel
from smolagents import CodeAgent, tool
# set env variable
load_dotenv()

# Tool definition
@tool
def get_weather(city: str) -> str:
    """Retrieves the current weather report for a specified city.
    Args:
        city (str): The name of the city to retrieve weather information for.
            Examples: "New York", "London", "Tokyo".
    """
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

# model setup
model = LiteLLMModel(model_id="sap/gpt-5")

# agent setup
agent = CodeAgent(tools=[get_weather], model=model)

response = agent.run("What is the weather like in London?")
print(response)
