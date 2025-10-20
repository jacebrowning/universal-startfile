# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from unittest.mock import patch

from startfile import startfile


def describe_startfile():
    @patch("subprocess.run")
    @patch("os.startfile", create=True)
    def with_file(mock_startfile, mock_call, tmp_path, expect):
        path = tmp_path / "example.txt"
        path.write_text("Hello, world!")

        startfile(path)
        expect(mock_startfile.call_count + mock_call.call_count) == 1

    @patch("subprocess.run")
    @patch("os.startfile", create=True)
    def with_non_existing_file(mock_startfile, mock_call, tmp_path, expect):
        path = tmp_path / "does not exist"

        startfile(path)
        expect(FileNotFoundError in (mock_startfile.side_effect, mock_call.side_effect))

    @patch("webbrowser.open")
    def with_url(mock_open, expect):
        startfile("http://example.com")
        expect(mock_open.call_count) == 1
