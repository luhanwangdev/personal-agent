from google.adk.agents import Agent, LlmAgent
from .tool_lib import calendar, weather


calendar_agent = Agent(
    name="calendar_agent",
    model="gemini-2.0-flash",
    description="Agent to manage calendar events.",
    instruction="You are a helpful agent who can help users manage calendar events. Your ONLY task is to manage calendar events. Do not engage in any other conversation or tasks.",
    tools=[calendar.get_calendar_events, calendar.create_calendar_event]
)

weather_time_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    # description="Agent to answer questions about the time and weather in a city.",
    description="You are a helpful agent who can answer user questions about the time and weather in a city. Your ONLY task is to answer questions about the time and weather in a city. Do not engage in any other conversation or tasks.",
    tools=[weather.get_weather, weather.get_current_time],
)

root_agent = LlmAgent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Main agent to manage calendar and weather events.",
    instruction="You are the main Agent, coordinating a team. - Your main task: Support most common use cases by delegating to specialized agents. - Delegation Rules: - If the user asks about weather or time (like 'What's the weather?', 'What time is it?'), delegate to `weather_time_agent`. - If the user asks about calendar, schedule, meetings, or appointments (like 'Schedule a meeting', 'What's on my calendar?'), delegate to `calendar_agent`. - For other queries, state clearly if you cannot handle them.",
    sub_agents=[calendar_agent, weather_time_agent]
)