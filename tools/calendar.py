def get_calendar_events(date: str):
    if date.lower() == "today":
        return {
            "status": "success",
            "report": (
                "You have a meeting with John Doe at 10:00 AM."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Calendar information for '{date}' is not available.",
        }

def create_calendar_event(title: str, start_time: str):
    return {
        "status": "success",
        "report": f"Event '{title}' created for {start_time}.",
    }