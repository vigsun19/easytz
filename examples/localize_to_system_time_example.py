from easytz.convert import localize_to_system_timezone
from datetime import datetime

## Example usage:
naive = datetime(2024, 10, 25, 12, 0, 0)  # Naive datetime without timezone
localized_dt = localize_to_system_timezone(naive)

print("Naive datetime:", naive)
print("Localized to system time zone:", localized_dt)
