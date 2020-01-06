from typing import IO, Sequence
from setuptools import setup, find_packages


def _description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


def _requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt", "r") as requirements:  # type: IO
        return tuple(map(str.strip, requirements.readlines()))


setup(
    name="async-weather-api",
    version="0.4.2",
    author="Volodymyr Yahello",
    author_email="vyahello@gmail.com",
    description=(
        "This project represents sample of asynchronous weather REST API that is build using **quart** "
        "(flask compatible API) python web microframework based on Asyncio"
    ),
    long_description=_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vyahello/async-weather-api",
    packages=find_packages(),
    include_package_data=True,
    install_requires=_requirements(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.6",
)
