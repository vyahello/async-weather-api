[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub version](https://badge.fury.io/gh/vyahello%2Fasync-weather-api.svg)](https://github.com/vyahello/async-weather-api/releases)
[![Build Status](https://travis-ci.org/vyahello/async-weather-api.svg?branch=master)](https://travis-ci.org/vyahello/async-weather-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/async-weather-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/async-weather-api?branch=master)

[![Forks](https://img.shields.io/github/forks/vyahello/async-weather-api)](https://github.com/vyahello/async-weather-api/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/async-weather-api)](https://github.com/vyahello/async-weather-api/stargazers)
[![Issues](https://img.shields.io/github/issues/vyahello/async-weather-api)](https://github.com/vyahello/async-weather-api/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/vyahello/async-weather-api.svg)](https://GitHub.com/vyahello/async-weather-api/graphs/watchers/)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/async-weather-api.svg)](https://GitHub.com/vyahello/async-weather-api/graphs/contributors/)

[![PyPI version shields.io](https://img.shields.io/pypi/v/async-weather-api.svg)](https://pypi.python.org/pypi/async-weather-api/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/async-weather-api.svg)](https://pypi.python.org/pypi/async-weather-api/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Async weather API
> This project represents sample of asynchronous weather REST API that is build using **quart** (flask compatible API) python web microframework based on Asyncio.


## Tools
- python 3.6 | 3.7 | 3.8
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [quart](https://pgjones.gitlab.io/quart/)
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [black](https://black.readthedocs.io/en/stable/)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)
  - [pydocstyle](http://www.pydocstyle.org/)

## Usage
Please run following script to obtain latest package from PYPI:
```bash
➜ pip install async-weather-api
```

Then please execute instructions below to launch game from your environment:
```python
import weather

weather.run(key="your-secret-key", bind="0.0.0.0:5001", debug=False)
Running on https://0.0.0.0:5001 (CTRL + C to quit)
...
```
> Note `key` stands for API key from https://openweathermap.org

### Endpoints
- **/** - home page
  ```bash
  ➜  curl -X GET http://0.0.0.0:5001/ 
  ➜  curl -X GET http://0.0.0.0:5001/index 
  ```
  **Response**: html page
- **/api/weather/{city}/{state}/{country}** - current weather event
    ```bash
  ➜  curl -X GET http://0.0.0.0:5001/api/events/London/GB/GreatBritain
  ```
  **Response**: json object
  ```json
  {"city":"London","country":"GreatBritain","name":"Jeff the player","state":"GB"}
  ```
- **/api/weather/{zip_code}/{country}** - current weather in city
  ```bash
  ➜  curl -X GET http://0.0.0.0:5001/api/weather/97002/us
  ```
  **Response**: json object
  ```json
  {"base":"stations","clouds":{"all":90},"cod":200,"coord":{"lat":45.23,"lon":-122.8},
  ...}
  ```
- **/api/sun/{zip_code}/{country}** - current sunset/sunrise in city
  ```bash
  ➜  curl -X GET http://0.0.0.0:5001/sun/weather/97002/us
  ```
  **Response**: json object
  ```json
  {"astronomical_twilight_begin":"04:03:49 PM","astronomical_twilight_end":"04:29:50 AM",
  ...}
  ```

## Development notes

### Run from source code

To be able to run source code please execute command below:
```bash
➜ python -m weather run --bind 0.0.0.0:5001 --mode prod --key your-secret-key
Running on https://0.0.0.0:5001 (CTRL + C to quit)
...
```

### CI 

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `mypy`, `pydocstyle`, `pylint`, `flake8`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
➜ ./analyse-code.sh
```
Also `test-report.html` will be generated after unittests execution.

### Release notes

* 0.4.0
  * Introduce PYPI package
* 0.3.0
  * Introduce asynchronous approach
* 0.2.0
  * Introduce synchronous approach
* 0.1.0
  * Distribute initial project version

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies
