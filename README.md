# easytz

**easytz** is a simple and efficient Python library for seamless time zone conversions and batch processing of datetime objects. Whether you're converting individual datetime objects across different time zones or handling multiple datetime conversions in one go, **easytz** makes it fast and straightforward.

## Features

- **Convert a single datetime object** between any two time zones.
- **Batch convert** a list of datetimes from their respective time zones to a target time zone.
- **Batch conversion to multiple time zones** from a single datetime object.
- **Localize a naive datetime** to the system's local time zone.

## Installation

To install **Easytz**, simply use pip:

```bash
pip install easytz

```
## Usage Examples
**1. Convert a single datetime object between two time zones**

```bash
from datetime import datetime
import pytz
from easytz import convert_time

dt = datetime(2024, 10, 25, 12, 0)  # Naive datetime
from_tz = 'America/New_York'
to_tz = 'Europe/London'

converted_time = convert_time(dt, from_tz, to_tz)
print(converted_time)  # Output: 2024-10-25 17:00:00+01:00

```
**2. Batch convert a single datetime to multiple time zones**

```bash
from easytz import batch_convert_to_multiple_timezones

# Create a timezone-aware datetime object
dt = datetime(2024, 10, 25, 15, 0, 0, tzinfo=pytz.UTC)

# List of target time zones to convert the datetime to
target_timezones = ['Europe/London', 'Asia/Tokyo', 'America/New_York']

converted_times = batch_convert_to_multiple_timezones(dt, target_timezones)
print(converted_times)

```
**3. Batch convert a list of datetimes to a target time zone**

```bash
from easytz import batch_convert_times

# List of datetime objects from different time zones
times_list = [
    {'time': '2024-10-25 12:00:00', 'from_tz': 'America/New_York'},
    {'time': '2024-10-25 12:00:00', 'from_tz': 'Europe/London'}
]

# The target time zone you want to convert all times to
target_timezone = 'Asia/Tokyo'

converted_times = batch_convert_times(times_list, target_timezone)
print(converted_times)

```
**4. Localize a naive datetime to the system's local time zones**

```bash
from easytz import localize_to_system_timezone

dt = datetime(2024, 10, 25, 12, 0)  # Naive datetime
localized_dt = localize_to_system_timezone(dt)
print(localized_dt)

```
## Contributing to easytz
Contributions to **easytz** are welcome! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.


### How to Contribute

1. **Fork the Repository**:  
   Start by forking the [easytz repository](https://github.com/vigsun19/easytz).

2. **Make Your Changes**:  
   Make the necessary changes, whether it's fixing a bug, adding a new feature, or improving documentation.

3. **Submit a Pull Request**:  
   Once your changes are ready, submit a pull request with a clear description of what you've done. Be sure to include relevant details, such as any bugs fixed or features added.

### Code of Conduct

By contributing, you agree to follow the Code of Conduct, ensuring a positive environment for all.

---
