__author__ = 'KoicsD'
import event_reg
from datetime import date, time
import unittest


class MyTestCase(unittest.TestCase):
    def test_EndTime_6_33_when_StartTime_18_00_onDate_2015_12_21_Raises(self):
        start_time = time(18)
        my_date = date(2015,12,21)
        my_string = "6:33"
        with self.assertRaises(ValueError) as my_err:
            event_reg.Donation.parse_end_time(my_string, my_date, start_time)
        self.assertEqual(my_err.exception.args, ("Preparation Time exceeds Duration or Duration is negative!",))


if __name__ == '__main__':
    unittest.main()
