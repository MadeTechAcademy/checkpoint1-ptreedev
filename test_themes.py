from unittest.mock import patch, mock_open, call
from jinja2 import Environment, FileSystemLoader
from themes import print_duties, write_html, format_html, duty_dict

def format_test_html():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("duties_template.html")
    rendered = template.render(duties = duty_dict.values())
    return rendered


def test_print_duties_prints_all_duties():
    with patch("builtins.print") as mock_print:
        print_duties(1)
        assert mock_print.call_count == 13
        for duty in duty_dict.values():
            mock_print.assert_any_call("{0}\n".format(duty))


def test_opt_boot_camp_prints_duty_1_2_3_4_13():
      with patch("builtins.print") as mock_print:
        print_duties(4)
        assert mock_print.call_count == 5
        calls = [call(duty_dict[1]), call(duty_dict[2]), call(duty_dict[3]), call(duty_dict[4]), call(duty_dict[13])]
        mock_print.assert_has_calls(calls)

def test_opt_Automate_prints_duty_5_7_10():
    with patch("builtins.print") as mock_print:
        print_duties(5)
        assert mock_print.call_count == 3
        calls = [call(duty_dict[5]),call(duty_dict[7]),call(duty_dict[10])]
        mock_print.assert_has_calls(calls)

def test_opt_Houston_prints_6_7_10_12():
    with patch("builtins.print") as mock_print:
        print_duties(6)
        assert mock_print.call_count == 4
        calls = [call(duty_dict[6]),call(duty_dict[7]),call(duty_dict[10]), call(duty_dict[12])]
        mock_print.assert_has_calls(calls)

def test_going_deeper_prints_11():
    with patch("builtins.print") as mock_print:
        print_duties(7)
        assert mock_print.call_count == 1
        mock_print.assert_called_once_with(duty_dict[11])

def test_Assemble_prints_8():
    with patch("builtins.print") as mock_print:
        print_duties(8)
        assert mock_print.call_count == 1
        mock_print.assert_called_once_with(duty_dict[8])

def test_format_html():
    assert format_html() == format_test_html()

def test_write_html_with_pytest_tmp(tmp_path):
    input_html = format_test_html()
    file_path = tmp_path / "output.html"

    write_html(input_html, str(file_path))

    content = file_path.read_text(encoding="utf-8")
    assert "<h1>Apprenticeship Duties</h1>" in content
    assert "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage." in content
    assert content.startswith("<html>")
    assert content.endswith("</html>")

# def test_write_duties_creates_html_file():
#     with patch("builtins.open", mock_open(), create=True) as open_mock:
#         write_duties()
#     expected_html = format_test_html(0)
#     open_mock.assert_called_with("file.html", "w")
#     open_mock.return_value.write.assert_any_call(expected_html)

# def test_opt_call_security_writes_duty_9():
#     with patch("builtins.open", mock_open(), create=True) as open_mock:
#             write_duties()
#             expected_html = format_test_html(1)
#             open_mock.assert_called_with("file.html", "w")
#             open_mock.return_value.write.assert_any_call(expected_html)