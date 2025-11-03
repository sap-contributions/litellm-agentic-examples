"""
A Langchain agent that uses a weather tool.
This example uses the Langgraph Functional API according to: https://docs.langchain.com/oss/python/langgraph/quickstart#use-the-functional-api
"""

from langchain.tools import tool
from langchain_litellm import ChatLiteLLM
from langgraph.graph import add_messages
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    ToolCall,
)
from langchain_core.messages import BaseMessage
from langgraph.func import entrypoint, task

# Step 1: Define model and tools

model = ChatLiteLLM(model="sap/gpt-4o", temperature=0)

# Define weather tool


@tool
def get_weather(city: str):
    """
    Returns weather information for a given city.
    :param city:
    :return: weather information
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


# Augment the LLM with tools

tools = [get_weather]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

# Step 2: Define model node


@task
def call_llm(messages: list[BaseMessage]):
    """LLM decides whether to call a tool or not"""
    return model_with_tools.invoke(
        [
            SystemMessage(
                content="You are a helpful weather assistant. "
                "When the user asks you about a specific city, "
                "use the 'get_weather' tool to find the information about the weather. "
                "Answer with a TV weather report in two sentences, including a small joke."
            )
        ]
        + messages
    )


# Step 3: Define tool node


@task
def call_tool(tool_call: ToolCall):
    """Performs the tool call"""
    tool = tools_by_name[tool_call["name"]]
    return tool.invoke(tool_call)


# Step 4: Define agent


@entrypoint()
def agent(messages: list[BaseMessage]):
    model_response = call_llm(messages).result()

    while True:
        if not model_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in model_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]
        messages = add_messages(messages, [model_response, *tool_results])
        model_response = call_llm(messages).result()

    messages = add_messages(messages, model_response)
    return messages


# Invoke
city = input("Input city: ")
input_message = [HumanMessage(content=f"What's the weather in {city}?")]
for chunk in agent.stream(input_message, stream_mode="updates"):
    print(chunk)
    print("\n")
