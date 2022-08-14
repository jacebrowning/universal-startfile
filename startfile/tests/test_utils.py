# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison,unused-argument

from startfile import startfile


def describe_startfile():
    def with_url(expect):
        startfile("http://exaple.com")
