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

## Usage

The system uses Google's ADK framework with Gemini 2.0 Flash model. The root agent automatically routes requests to appropriate specialized agents based on the query type.

### Supported Operations

**Calendar Operations:**

- View calendar events for today or specific dates
- Real-time integration with Google Calendar API
- Create new calendar events (in development)

**Weather & Time Operations:**

- Get weather information for supported cities
- Get current time for supported cities

### Example Interactions

- "What's on my calendar today?"
- "Show me my calendar for 2024-12-25"
- "Schedule a meeting with John at 2 PM"
- "What's the weather in New York?"
- "What time is it in New York?"

## Current Limitations

- **Calendar**: Event creation is not yet implemented (read-only functionality)
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
