import unittest
from unittest.mock import patch

from themes import print_duties, duty_list

# are the tests and naming conventions verbose?

def test_print_duties_prints_all_duties():
    with patch("builtins.print") as mock_print:
        print_duties()
        assert mock_print.call_count == 13
        for duty in duty_list:
            mock_print.assert_any_call("{0}\n".format(duty))