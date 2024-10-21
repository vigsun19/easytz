from easytz.convert import batch_convert_to_multiple_timezones
from datetime import datetime
import pytz

# Event time in UTC
event_time = datetime(2024, 10, 25, 15, 0, 0, tzinfo=pytz.UTC)

# List of time zones to convert to
target_timezones = ['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

# Convert the event time to all these time zones
converted_times = batch_convert_to_multiple_timezones(event_time, target_timezones)

# Print the results
for time_data in converted_times:
    print(f"Event time in {time_data['to_tz']}: {time_data['converted_time']}")