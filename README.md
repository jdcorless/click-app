# click-app

[![PyPI](https://img.shields.io/pypi/v/click-app.svg)](https://pypi.org/project/click-app/)
[![Changelog](https://img.shields.io/github/v/release/jdcorless/click-app?include_prereleases&label=changelog)](https://github.com/jdcorless/click-app/releases)
[![Tests](https://github.com/jdcorless/click-app/workflows/Test/badge.svg)](https://github.com/jdcorless/click-app/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/jdcorless/click-app/blob/master/LICENSE)

Built from simonw template

## Installation

Install this tool using `pip`:

    pip install click-app

## Usage

For help, run:

    click-app --help

You can also use:

    python -m click_app --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd click-app
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
