from easytz.convert import batch_convert_times
from datetime import datetime
import pytz

# List of datetimes from different time zones
times_to_convert = [
    {"time": "2024-10-01 12:00:00", "from_tz": "America/New_York"},
    {"time": "2024-10-01 12:00:00", "from_tz": "Europe/London"},
    {"time": "2024-10-01 12:00:00", "from_tz": "Asia/Tokyo"}
]

# Convert naive datetime strings to timezone-aware datetime objects
for time_data in times_to_convert:
    time_str = time_data["time"]
    from_tz = time_data["from_tz"]

    # Parse the time string into a naive datetime object
    naive_dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

    # Get the timezone object for the source time zone
    timezone = pytz.timezone(from_tz)

    # Localize the naive datetime to the source timezone
    aware_dt = timezone.localize(naive_dt)

    # Replace the naive time with the timezone-aware time
    time_data["time"] = aware_dt

# Print the localized times to check if data is intact
print("After Localization:", times_to_convert)

# Convert all of the times to UTC
converted_times = batch_convert_times(times_to_convert, to_tz="UTC")

# Print the results
for time_data in converted_times:
    print(f"Original time: {time_data['original_time']} in {time_data['from_tz']}")
    print(f"Converted time to UTC: {time_data['converted_time']}")
