from unittest.mock import patch, mock_open
from themes import print_duties, duty_list, write_duties

# are the tests and naming conventions verbose?

def test_print_duties_prints_all_duties():
    with patch("builtins.print") as mock_print:
        print_duties()
        assert mock_print.call_count == 13
        for duty in duty_list:
            mock_print.assert_any_call("{0}\n".format(duty))


def test_write_duties_creates_file():
    with patch("themes.open", mock_open(), create=True) as open_mock:
        write_duties()
    assert open_mock.call_count == 1
    open_mock.assert_called_with("file.txt", "x")