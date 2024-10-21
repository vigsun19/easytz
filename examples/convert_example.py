from easytz.convert import convert_time
from datetime import datetime
import pytz

# Create a naive datetime object (without timezone)
naive_time = datetime(2024, 10, 25, 15, 0, 0)

# Make the naive datetime object timezone-aware (in UTC)
event_time = pytz.utc.localize(naive_time)

# Convert the event time from UTC to New York time
new_york_time = convert_time(event_time, 'UTC', 'America/New_York')

print(f"Original event time (UTC): {event_time}")
print(f"Converted event time (New York): {new_york_time}")