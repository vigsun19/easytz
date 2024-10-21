from easytz.convert import convert_time
from datetime import datetime
import pytz

# Create a timezone-aware datetime object directly
from_tz = 'America/New_York'
dt = datetime(2024, 10, 25, 12, 0, 0, tzinfo=pytz.timezone(from_tz))

# Convert to another time zone (only provide the target timezone)
to_tz = 'Europe/London'
converted_time = convert_time(dt, to_tz=to_tz)  # No need to pass from_tz

# Print the result
print(converted_time)  # Output: 2024-10-25 17:00:00+01:00