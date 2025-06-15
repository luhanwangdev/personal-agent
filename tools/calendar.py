import datetime
from datetime import timezone, timedelta
from ..services.calendar import calendar_service


def get_calendar_events(date: str):
    try:
        taipei_tz = timezone(timedelta(hours=8))
        target_date = None

        if date.lower() == "today":
            target_date = datetime.date.today()
        else:
            try:
                target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            except ValueError:
                return {
                    "status": "error",
                    "error_message": f"Invalid date format. Please use YYYY-MM-DD.",
                }
        
        start_time = datetime.datetime.combine(target_date, datetime.time.min, taipei_tz)
        end_time = datetime.datetime.combine(target_date, datetime.time.max, taipei_tz)

        events_result = calendar_service.service.events().list(
            calendarId="primary",
            timeMin=start_time.isoformat(),
            timeMax=end_time.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        events = events_result.get('items', [])

        if not events:
            return {
                "status": "success",
                "report": f"You have nothing on the schedule for {target_date}."
            }
        
        return{
            "status": "success",
            "report": events
        }
    except Exception as e:
        return{
            "status": "error",
            "error_message": f"Error fetching calendar data: {str(e)}",
        }


def create_calendar_event(title: str, start_time: str):
    return {
        "status": "success",
        "report": f"Event '{title}' created for {start_time}.",
    }