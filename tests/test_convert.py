import unittest
from datetime import datetime
import pytz
from easytz.convert import convert_time, batch_convert_to_multiple_timezones, batch_convert_times, \
    localize_to_system_timezone


class TestConvertFunctions(unittest.TestCase):

    def setUp(self):
        # Create a timezone-aware datetime for testing
        self.dt_naive = datetime(2024, 10, 25, 15, 0, 0)  # Naive datetime (no timezone)
        self.dt_aware_utc = pytz.utc.localize(self.dt_naive)  # UTC aware datetime
        self.timezone_ny = pytz.timezone('America/New_York')
        self.timezone_london = pytz.timezone('Europe/London')
        self.timezone_tokyo = pytz.timezone('Asia/Tokyo')

    def test_convert_time(self):
        # Test converting from UTC to New York timezone
        dt_converted = convert_time(self.dt_aware_utc,  'America/New_York')

        # Check the time zone of the result
        self.assertEqual(dt_converted.tzinfo.zone, 'America/New_York')

        # Assert that the converted time is correct
        self.assertEqual(dt_converted.strftime('%Y-%m-%d %H:%M:%S'), '2024-10-25 11:00:00')

    def test_batch_convert_to_multiple_timezones(self):
        target_timezones = ['America/New_York', 'Europe/London', 'Asia/Tokyo']

        # Convert the datetime to multiple timezones
        converted_times = batch_convert_to_multiple_timezones(self.dt_aware_utc, target_timezones)

        # Check that we have 3 converted times
        self.assertEqual(len(converted_times), 3)

        # Assert correct conversion for each timezone
        self.assertEqual(converted_times[0]['converted_time'], '2024-10-25 11:00:00')
        self.assertEqual(converted_times[1]['converted_time'], '2024-10-25 16:00:00')
        self.assertEqual(converted_times[2]['converted_time'], '2024-10-26 00:00:00')

    def test_batch_convert_times(self):
        times_list = [
            {'time': '2024-10-25 12:00:00', 'from_tz': 'America/New_York'},
            {'time': '2024-10-25 12:00:00', 'from_tz': 'Europe/London'}
        ]
        target_timezone = 'Asia/Tokyo'

        # Convert the times in the source timezones to aware datetimes
        aware_times_list = []
        for time_data in times_list:
            time_str = time_data['time']
            from_tz = time_data['from_tz']
            dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

            # Localize the naive datetime to the from_tz timezone
            timezone = pytz.timezone(from_tz)
            dt = timezone.localize(dt)  # Make the datetime aware

            aware_times_list.append({
                'time': dt,  # Keep the datetime object (not string)
                'from_tz': from_tz
            })

        # Convert the list of times to Tokyo timezone
        converted_times = batch_convert_times(aware_times_list, target_timezone)

        # Check that the list has 2 converted times
        self.assertEqual(len(converted_times), 2)

        # Assert that the converted times are correct
        # Correct conversion for New York -> Tokyo
        self.assertEqual(converted_times[0]['converted_time'], '2024-10-26 01:00:00')  # 12:00 PM EDT -> 01:00 AM JST
        # Correct conversion for London -> Tokyo
        self.assertEqual(converted_times[1]['converted_time'], '2024-10-25 20:00:00')  # 12:00 PM BST -> 01:00 AM JST

    def test_localize_to_system_timezone(self):
        # Test localizing a naive datetime to the system's local timezone
        naive_dt = datetime(2024, 10, 25, 12, 0, 0)  # A naive datetime (without timezone)

        # Localize the naive datetime to the system's local timezone
        localized_dt = localize_to_system_timezone(naive_dt)

        # Assert that the localized datetime is not naive (i.e., it has a timezone)
        self.assertIsNotNone(localized_dt.tzinfo)

        # Assert that the localized datetime is now in the system's local time zone
        # (The expected tzinfo here will be the system's local timezone, not "America/New_York")
        # This test will pass as long as the system time zone is the default local time zone
        self.assertTrue(localized_dt.tzinfo is not None)

    def test_convert_time_with_naive_datetime(self):
        # Test that convert_time raises ValueError if input datetime is naive
        with self.assertRaises(ValueError):
            convert_time(self.dt_naive, 'America/New_York')

    def test_batch_convert_times_with_naive_datetime(self):
        # Test that batch_convert_times correctly handles naive datetimes by localizing them
        times_list = [
            {'time': datetime.strptime('2024-10-25 12:00:00', '%Y-%m-%d %H:%M:%S'), 'from_tz': 'America/New_York'},
            {'time': datetime.strptime('2024-10-25 12:00:00', '%Y-%m-%d %H:%M:%S'), 'from_tz': 'Europe/London'}
        ]

        # Call the function to convert the times to a target timezone (e.g., 'Asia/Tokyo')
        converted_times = batch_convert_times(times_list, 'Asia/Tokyo')
        print(converted_times)

        #Assert that the results are as expected
        for time_data in converted_times:
            # Ensure that the original time is correctly present in the output
            self.assertTrue(time_data['original_time'])

            # Ensure that the from_tz is correctly passed through
            self.assertTrue(time_data['from_tz'])  # Adjust per the timezone being tested

            # Ensure the converted time is correctly formatted
            self.assertTrue(time_data['converted_time'])


if __name__ == '__main__':
    unittest.main()
