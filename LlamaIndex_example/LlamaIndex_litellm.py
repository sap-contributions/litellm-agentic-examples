# pip install llama-cloud-services python-dotenv
# pip install llama-index-llms-litellm
# pip install llama-index
import asyncio
from llama_index.llms.litellm import LiteLLM
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool

# set env variable
load_dotenv()

# Tool definition
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
    city_normalized = city.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


tool = FunctionTool.from_defaults(
    get_weather
)

message = ChatMessage(role="user", content="What is the weather like in London?")


# llm setup
llm = LiteLLM("sap/gpt-5",
              temperature=1,)

# agent setup
agent = ReActAgent(llm=llm, tools=[tool])


async def main():
    response = await agent.run(user_msg=message)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
