from crewai import Agent, Task, Crew
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()


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
    llm="sap/gpt-4o",
    tools=[get_weather],
    allow_delegation=False,
)


# --- Define tasks ---
agent_task = Task(
    description=(
        f"Write a couple sentences for TV weather report in {city} including a small joke."
    ),
    expected_output=(
        "Good quality text of two sentences about weather with small joke."
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
