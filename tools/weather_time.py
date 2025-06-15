import datetime
import aiohttp
import os
from zoneinfo import ZoneInfo

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

async def get_weather(city: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
            async with session.get(url) as response:
                data = await response.json()
                result = data.get("current", {})
                if result:
                    return {
                        "status": "success",
                        "report": result,
                    }
                else:
                    return {
                        "status": "error",
                        "error_message": f"Weather information for '{city}' is not available.",
                    }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching weather data: {str(e)}",
        }


async def get_current_time(city: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
            async with session.get(url) as response:
                data = await response.json()
                result = data.get("location", {})
                if result:
                    return {
                        "status": "success",
                        "localtime": result.get("localtime", ""),
                        "localtime_epoch": result.get("localtime_epoch", ""),
                    }
                else:
                    return {
                        "status": "error",
                        "error_message": f"Weather information for '{city}' is not available.",
                    }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching current time data: {str(e)}",
        }