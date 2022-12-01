from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="click-app",
    description="Built from simonw template",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="John D. Corless",
    url="https://github.com/jdcorless/click-app",
    project_urls={
        "Issues": "https://github.com/jdcorless/click-app/issues",
        "CI": "https://github.com/jdcorless/click-app/actions",
        "Changelog": "https://github.com/jdcorless/click-app/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["click_app"],
    entry_points="""
        [console_scripts]
        click-app=click_app.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
