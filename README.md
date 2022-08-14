# Overview

A cross-platform version of [os.startfile](https://docs.python.org/3/library/os.html#os.startfile) from the standard library.

[![Unix Build Status](https://img.shields.io/github/workflow/status/jacebrowning/universal-startfile/main)](https://github.com/jacebrowning/universal-startfile/actions)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/universal-startfile.svg?label=windows)](https://ci.appveyor.com/project/jacebrowning/universal-startfile)
[![Coverage Status](https://img.shields.io/codecov/c/gh/jacebrowning/universal-startfile)](https://codecov.io/gh/jacebrowning/universal-startfile)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/universal-startfile.svg)](https://scrutinizer-ci.com/g/jacebrowning/universal-startfile)
[![PyPI License](https://img.shields.io/pypi/l/universal-startfile.svg)](https://pypi.org/project/universal-startfile)
[![PyPI Version](https://img.shields.io/pypi/v/universal-startfile.svg)](https://pypi.org/project/universal-startfile)
[![PyPI Downloads](https://img.shields.io/pypi/dm/universal-startfile.svg?color=orange)](https://pypistats.org/packages/universal-startfile)

## Setup

### Requirements

* Python 3.7+

### Installation

Install it directly into an activated virtual environment:

```text
$ pip install universal-startfile
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add universal-startfile
```

## Usage

After installation, use the `startfile` function:

```text
$ python
>>> from startfile import startfile
>>> startfile("~/Downloads/example.png")
>>> startfile("http://example.com)
```
