from dotenv import load_dotenv
import asyncio
import warnings
import logging

# Setup
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)
load_dotenv()

# ADK imports
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types


# Tool definition
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
    city_normalized = city.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25°C.",
        },
        "london": {
            "status": "success",
            "report": "It's cloudy in London with a temperature of 15°C.",
        },
        "tokyo": {
            "status": "success",
            "report": "Tokyo is experiencing light rain and a temperature of 18°C.",
        },
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have weather information for '{city}'.",
        }


# Model selection
model = LiteLlm(model="sap/gpt-4.1")

# Weather agent
weather_agent = Agent(
    name="weather_agent",
    model=model,
    description=f"Prepare a couple sentences TV speach about weather in the given city, "
                f"using information from run the get_weather tool",
    instruction="You are a helpful weather assistant. "
                "When the user asks for the weather in a specific city, "
                "use the 'get_weather' tool to find the information. "
                "If the tool returns an error, inform the user politely. "
                "If the tool is successful, write a couple sentences for a "
                "TV weather report in the given city including a small joke.",
    tools=[get_weather],
)


# Helper function
async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response."""

    content = types.Content(role="user", parts=[types.Part(text=query), types.Part()])
    final_response_text = "Agent did not produce a final response."

    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = (
                    f"Agent escalated: {event.error_message or 'No specific message.'}"
                )
            break

    print(f"Agent Response: {final_response_text}")


# Main conversation
async def run_conversation():
    session_service = InMemorySessionService()

    APP_NAME = "weather_tutorial_app"
    USER_ID = "user_1"
    SESSION_ID = "session_001"

    session = await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    runner = Runner(
        agent=weather_agent, app_name=APP_NAME, session_service=session_service
    )
    city = input("Input city: ")
    await call_agent_async(
        f"What is the weather like in {city}?",
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )


# Run
if __name__ == "__main__":
    asyncio.run(run_conversation())
