from datetime import datetime
import pytz

def convert_time(dt, to_tz):
    """
    Convert a datetime object from its timezone to another time zone.

    Args:
    - dt (datetime): The timezone-aware datetime object to convert.
    - to_tz (str): The target time zone (e.g., 'Europe/London').

    Returns:
    - datetime: The converted datetime object in the target time zone.
    """
    if dt.tzinfo is None:
        raise ValueError("The input datetime must be timezone-aware.")

    # Directly use the current tzinfo of dt
    from_timezone = dt.tzinfo
    to_timezone = pytz.timezone(to_tz)

    # Convert the datetime to the target timezone
    dt_to = dt.astimezone(to_timezone)

    return dt_to

def batch_convert_to_multiple_timezones(dt, target_timezones):
    """
    Convert a single datetime object to a list of time zones.

    Args:
    - dt (datetime): The timezone-aware datetime object to convert.
    - target_timezones (list of str): A list of time zones to convert to.

    Returns:
    - list of dicts: A list of dictionaries with the original datetime and its conversions to each time zone.
    """
    if dt.tzinfo is None:
        raise ValueError("The input datetime must be timezone-aware.")

    converted_times = []

    for tz in target_timezones:
        # Convert the datetime to the target time zone
        converted_time = convert_time(dt, tz)  # We no longer pass the from_tz (since it's already timezone-aware)

        # Append the conversion result
        converted_times.append({
            'original_time': dt.strftime('%Y-%m-%d %H:%M:%S'),
            'from_tz': dt.tzinfo.zone,
            'converted_time': converted_time.strftime('%Y-%m-%d %H:%M:%S'),
            'to_tz': tz
        })

    return converted_times


def batch_convert_times(times_list, to_tz):
    """
    Convert a list of datetime objects from their respective time zones to the target time zone.

    Args:
    - times_list (list of dicts): A list of dictionaries where each dictionary contains:
      - 'time' (str or datetime): A datetime string or datetime object.
      - 'from_tz' (str): The source time zone of the datetime.
    - to_tz (str): The target time zone to convert all times to.

    Returns:
    - list of dicts: A list of dictionaries with converted times.

    Raises:
    - ValueError: If any datetime is naive (lacking timezone info).
    """
    converted_times = []

    for time_data in times_list:
        time_value = time_data['time']
        from_tz = time_data['from_tz']

        # If time is a string, parse it into a datetime object
        if isinstance(time_value, str):
            dt = datetime.strptime(time_value, '%Y-%m-%d %H:%M:%S')
        elif isinstance(time_value, datetime):
            dt = time_value  # Already a datetime object
        else:
            raise ValueError(f"Unexpected time format: {time_value}")

        # Ensure the datetime object is timezone-aware by localizing if naive
        if dt.tzinfo is None:
            # Localize the naive datetime using the 'from_tz' time zone
            timezone = pytz.timezone(from_tz)
            dt = timezone.localize(dt)
        else:
            # If the datetime is already timezone-aware, ensure it's in the correct 'from_tz' timezone
            dt = dt.astimezone(pytz.timezone(from_tz))

        # Convert the datetime to the target time zone (to_tz)
        target_timezone = pytz.timezone(to_tz)
        converted_dt = dt.astimezone(target_timezone)

        # Append the conversion result
        converted_times.append({
            'original_time': time_value,  # Keep original time for reference
            'from_tz': from_tz,           # Keep the source timezone for reference
            'converted_time': converted_dt.strftime('%Y-%m-%d %H:%M:%S'),  # Use converted time
            'to_tz': to_tz                # Keep the target timezone for reference
        })

    return converted_times


def localize_to_system_timezone(dt):
    """
    Localize a naive datetime to the system's local time zone.

    Args:
    - dt (datetime): A naive datetime object to localize.

    Returns:
    - datetime: The datetime object localized to the system's local time zone.
    """
    return dt.astimezone()

