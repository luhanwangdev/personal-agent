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
- View today's calendar events
- Create new calendar events

**Weather & Time Operations:**
- Get weather information for supported cities
- Get current time for supported cities

### Example Interactions

- "What's on my calendar today?"
- "Schedule a meeting with John at 2 PM"
- "What's the weather in New York?"
- "What time is it in New York?"

## Current Limitations

- Calendar data is currently mocked (only supports "today" queries)
- Weather and time information only available for New York
- No persistent storage for calendar events

## Project Structure

```
├── agent.py              # Main agent definitions
├── tool_lib/             # Tool implementations
│   ├── calendar.py       # Calendar management tools
│   └── weather.py        # Weather and time tools
├── requirements.txt      # Python dependencies
└── __init__.py          # Package initialization
```