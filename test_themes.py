from unittest.mock import patch, mock_open, call
from themes import print_duties, duty_list, write_duties, format_html

# are the tests and naming conventions verbose?
def format_test_html():
    expected_lines = [
        "<html>",
        "    <head>",
        "        <meta charset=\"UTF-8\"/>",
        "        <title>Apprenticeship Duties</title>",
        "    </head>",
        "    <body>",
        "        <h1>Apprenticeship Duties</h1>",
        "        <ol>"
    ]
    expected_lines += [f"            <li>{duty}</li>" for duty in duty_list]
    expected_lines += [
        "        </ol>",
        "    </body>",
        "</html>"
    ]
    expected_html = "\n".join(expected_lines)
    return expected_html

def test_print_duties_prints_all_duties():
    with patch("builtins.print") as mock_print:
        print_duties(1)
        assert mock_print.call_count == 13
        for duty in duty_list:
            mock_print.assert_any_call("{0}\n".format(duty))

def test_opt_call_security_prints_duty_9():
      with patch("builtins.print") as mock_print:
        print_duties(3)
        assert mock_print.call_count == 1
        mock_print.assert_called_once_with(duty_list[8])

def test_opt_boot_camp_prints_duty_1_2_3_4_13():
      with patch("builtins.print") as mock_print:
        print_duties(4)
        assert mock_print.call_count == 5
        calls = [call(duty_list[0]), call(duty_list[1]), call(duty_list[2]), call(duty_list[3]), call(duty_list[12])]
        mock_print.assert_has_calls(calls)

def test_format_html():
    assert format_html() == format_test_html()

def test_write_duties_creates_html_file():
    with patch("builtins.open", mock_open(), create=True) as open_mock:
        write_duties()
    expected_html = format_test_html()
    assert open_mock.call_count == 1
    open_mock.assert_called_with("file.html", "w")
    open_mock.return_value.write.assert_any_call(expected_html)
