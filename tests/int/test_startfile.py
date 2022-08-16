import os

import pytest

from startfile import startfile


@pytest.mark.skipif("CI" not in os.environ, reason="Only run on CI")
def test_startfile_with_url():
    startfile("http://example.com")
