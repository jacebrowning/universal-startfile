# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from unittest.mock import patch

from startfile import startfile


def describe_startfile():
    @patch("subprocess.call")
    @patch("os.startfile", create=True)
    def with_file(mock_startfile, mock_call, tmp_path, expect):
        path = tmp_path / "example.txt"
        path.write_text("Hello, world!")

        startfile(path)
        expect(mock_startfile.call_count + mock_call.call_count) == 1

    @patch("webbrowser.open")
    def with_url(mock_open, expect):
        startfile("http://exaple.com")
        expect(mock_open.call_count) == 1
