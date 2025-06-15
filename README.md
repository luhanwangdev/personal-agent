# ADK Multi-Agent System

A Google ADK (Agent Development Kit) project demonstrating a hierarchical multi-agent system for calendar and weather management.

## Overview

This project implements a coordinated agent system where a root agent delegates specialized tasks to domain-specific agents:

- **Calendar Agent**: Manages calendar events and scheduling
- **Weather Time Agent**: Provides weather information and current time for cities

## Architecture

```
Root Agent (Coordinator)
├── Calendar Agent
│   ├── get_calendar_events
│   └── create_calendar_event
└── Weather Time Agent
    ├── get_weather
    └── get_current_time
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up Google ADK:

Navigate to the parent directory and run:
```bash
cd ..
adk web
```

This will open the ADK web interface where you can:
- Configure your agents and tools
- Test agent interactions
- Monitor agent performance
- Deploy your multi-agent system

4. Configure Google Calendar API (optional):
   - Place your `credentials.json` file in the project root
   - The OAuth flow will run automatically on first calendar access

## Usage

The system uses Google's ADK framework with Gemini 2.0 Flash model. 

1. Start the ADK web interface from the parent directory:
```bash
cd ..
adk web
```

2. The root agent automatically routes requests to appropriate specialized agents based on the query type.

### Supported Operations

**Calendar Operations:**

- View calendar events for today or specific dates
- Create new calendar events with customizable duration and description
- Real-time integration with Google Calendar API

**Weather & Time Operations:**

- Get weather information for supported cities
- Get current time for supported cities

### Example Interactions

- "What's on my calendar today?"
- "Show me my calendar for 2024-12-25"
- "Schedule a meeting with John at 2024-12-15 14:30"
- "Create a 90-minute presentation event on 2024-12-20 10:00"
- "What's the weather in New York?"
- "What time is it in New York?"

## Current Limitations

- **Calendar**: Uses Taipei timezone (Asia/Taipei) for all events
- **Weather**: Weather and time information only available for New York
- **Authentication**: Manual OAuth flow required for initial setup

## Project Structure

```
├── agent.py              # Main agent definitions
├── services/             # Service implementations
│   └── calendar.py       # Google Calendar integration
├── tools/                # Tool implementations
│   ├── calendar.py       # Calendar management tools
│   └── weather_time.py   # Weather and time tools
├── credentials.json      # Google API credentials
├── token.json           # OAuth token storage
├── requirements.txt      # Python dependencies
└── __init__.py          # Package initialization
```
