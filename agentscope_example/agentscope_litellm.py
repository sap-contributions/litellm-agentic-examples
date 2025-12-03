# pip install agentscope
import os
import litellm
from dotenv import load_dotenv
from agentscope.model import OpenAIChatModel
from agentscope.tool import ToolResponse, Toolkit
from agentscope.message import TextBlock
from agentscope.agent import ReActAgent
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
import asyncio

# set env variable
litellm.use_litellm_proxy = True
load_dotenv()

api_base = os.getenv("PROXY_BASE_URL")
api_key = os.getenv("LITELLM_PROXY_API_KEY")

# tool definition
def get_weather(city: str) -> ToolResponse:
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
        return ToolResponse(content=[
            TextBlock(type="text",
                      text=mock_weather_db[city_normalized])
        ])
    else:
        return ToolResponse(content=[
            TextBlock(type="text",
                      text=f"The weather in {city} is sunny with a temperature of 20°C.")
        ])
# Register the tool function in a toolkit
toolkit = Toolkit()
toolkit.register_tool_function(get_weather)

# model setup
sap_model = OpenAIChatModel(model_name='sap/gpt-4o',
                        api_key=api_key,
                        client_args={"base_url": api_base},
                        stream=False)

agent = ReActAgent(
        name="weather agent",
        sys_prompt="You are a helpful weather assistant. "
                "When the user asks for the weather in a specific city, "
                "use the 'get_weather' tool to find the information. "
                "If the tool returns an error, inform the user politely. "
                "If the tool is successful, write a couple sentences for "
                "TV weather report in the city, that will be include small jok",
        model=sap_model,
        formatter=DashScopeChatFormatter(),
        toolkit=toolkit,
        memory=InMemoryMemory(),
    )

msg = Msg(
        name="user",
        content="What is the weather like in Tbilisi?",
        role="user",
    )

async def run_conversation():
    result = await agent(msg)
    print(result)

asyncio.run(run_conversation())
