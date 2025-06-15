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


def create_calendar_event(title: str, start_time: str, duration_minutes: int = 60, description: str = ""):
    try:
        taipei_tz = timezone(timedelta(hours=8))
        
        try:
            start_dt = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
            start_dt = start_dt.replace(tzinfo=taipei_tz)
            
        except ValueError:
            return {
                "status": "error",
                "error_message": "Invalid start_time format. Use 'YYYY-MM-DD HH:MM' or ISO format."
            }
        
        end_dt = start_dt + timedelta(minutes=duration_minutes)
        
        event = {
            'summary': title,
            'description': description,
            'start': {
                'dateTime': start_dt.isoformat(),
                'timeZone': 'Asia/Taipei',
            },
            'end': {
                'dateTime': end_dt.isoformat(),
                'timeZone': 'Asia/Taipei',
            },
        }
        
        created_event = calendar_service.service.events().insert(
            calendarId='primary', 
            body=event
        ).execute()
        
        return {
            "status": "success",
            "report": f"Event '{title}' created successfully from {start_dt.strftime('%Y-%m-%d %H:%M')} to {end_dt.strftime('%H:%M')} (Taipei time).",
            "event_id": created_event.get('id'),
            "event_link": created_event.get('htmlLink')
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error creating calendar event: {str(e)}",
        }