# https://docs.ag2.ai/latest/docs/user-guide/models/litellm-proxy-server/installation/
import os
import litellm
from dotenv import load_dotenv
from typing import Any
from autogen import ConversableAgent, LLMConfig
from autogen.agentchat.group.patterns import AutoPattern
from autogen.agentchat import initiate_group_chat

# set env variable
litellm.use_litellm_proxy = True
load_dotenv()

api_base = os.getenv("LITELLM_PROXY_URL")
api_key = os.getenv("LITELLM_MASTER_KEY")

# tool definition
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

# set up model
llm_config = LLMConfig(config_list={"model": "sap/gpt-4o", "base_url": api_base, "api_key": api_key})

#setup function for finish conversation
def is_termination_msg(msg: dict[str, Any]) -> bool:
    content = msg.get("content", "")
    return (content is not None) and "==== REPORT GENERATED ====" in content

# setup agent
assistant = ConversableAgent(name="assistant",
                             llm_config=llm_config,
                             system_message="You are a helpful weather assistant. "
                                            "When the user asks for the weather in a specific city, "
                                            "use the 'get_weather' tool to find the information. "
                                            "If the tool returns an error, inform the user politely. "
                                            "If the tool is successful, write a couple sentences for a "
                                            "TV weather report in the city, that will be include small joke."
                                            "Once you've generated the report append this to the summary:"
                                            "==== REPORT GENERATED ====",
                             functions=[get_weather])
# setup pattern
pattern = AutoPattern(initial_agent=assistant,
                      agents=[assistant],
                      group_manager_args={
                          "llm_config": llm_config,
                          "is_termination_msg": is_termination_msg
                      },
                      )
# start conversation
result, _, _ = initiate_group_chat(pattern=pattern,
                                   messages="What is the weather like in Tbilisi?",
                                   )
