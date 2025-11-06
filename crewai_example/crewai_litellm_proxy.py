import os

from crewai import Agent, Task, Crew
from crewai import LLM
from crewai.tools import tool
from dotenv import load_dotenv
import litellm

litellm.use_litellm_proxy = True
load_dotenv()

api_base = os.getenv("LITELLM_ROXY_URL")
api_key = os.getenv("LITELLM_MASTER_KEY")
proxy_llm = LLM(
    model="sap/gpt-4o", api_base=api_base, base_url=api_base, api_key=api_key
)


@tool("get_weather")
def get_weather(city: str) -> str:
    """Moke function"""
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


city = input("Input city: ")

# --- Define agents ---
agent = Agent(
    role="Weather presenter",
    goal=f"Prepare a couple sentences in TV speach about weather in the {city}, "
         f"using information from the get_weather tool",
    backstory="You are the weather presenter on TV.",
    llm=proxy_llm,
    tools=[get_weather],
    allow_delegation=False,
)

# --- Define tasks ---
agent_task = Task(
    description=(
        f"Write a couple sentences for TV weather report in {city}, that will be include small jok"
    ),
    expected_output=(
        "Good quality text of two sentences about weather and with small jok"
    ),
    agent=agent,
)

# --- Assemble crew ---
crew = Crew(
    agents=[agent],
    tasks=[agent_task],
    verbose=True,
)

# --- Run ---
result = crew.kickoff()
print("\n📘 Result:\n", result)
