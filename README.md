![Screenshot](logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/async-weather-api.svg)](https://pypi.python.org/pypi/async-weather-api/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/async-weather-api.svg)](https://pypi.python.org/pypi/async-weather-api/)
[![Downloads](https://pepy.tech/badge/async-weather-api)](https://pepy.tech/project/async-weather-api)
[![Build Status](https://travis-ci.org/vyahello/async-weather-api.svg?branch=master)](https://travis-ci.org/vyahello/async-weather-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/async-weather-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/async-weather-api?branch=master)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/async-weather-api.svg)](https://hub.docker.com/repository/docker/vyahello/async-weather-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Async weather API
> This project represents sample of asynchronous weather REST API that is build using **quart** (flask compatible API) python web microframework based on Asyncio.
>
> It uses https://openweathermap.org to obtain weather data.

## Tools

### Production
- python 3.6, 3.7, 3.8
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [quart](https://pgjones.gitlab.io/quart/)

### Development
- [pytest](https://pypi.org/project/pytest/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](http://www.pydocstyle.org/)

## Usage

### Quick start

Please run following script to obtain the latest package from PYPI:
```bash
pip install async-weather-api
```

Then please execute steps below to launch API from your environment:
```python
import weather

weather.run(key="your-secret-key", bind="0.0.0.0:5001", debug=False)
```
> Note: `key` stands for API key from https://openweathermap.org

### Docker image

Please run next command to start async weather api via docker:
```bash
docker run -it -p 3000:5001 vyahello/async-weather-api:0.5.0 \
  weather run \
  --bind 0.0.0.0:5001 \
  --mode prod \
  --key <secret-key>
```

> Note: please use `3000` port to access application via docker

### Source code

To be able to run source code please execute command below:
```bash
python -m weather run --bind 0.0.0.0:5001 --mode prod --key your-secret-key
```

### Endpoints
- **/** - home page
  ```bash
  curl -X GET http://0.0.0.0:5001/ 
  curl -X GET http://0.0.0.0:5001/index 
  ```
  _Response_: html page
  
- **/api/weather/{city}/{state}/{country}** - current weather event
  ```bash
  curl -X GET http://0.0.0.0:5001/api/events/London/GB/GreatBritain
  ```
  _Response_: json object
  ```json
  {"city":"London","country":"GreatBritain","name":"Jeff the player","state":"GB"}
  ```
  
- **/api/weather/{zip_code}/{country}** - current weather in city
  ```bash
  curl -X GET http://0.0.0.0:5001/api/weather/97002/us
  ```
  _Response_: json object
  ```json
  {"base":"stations","clouds":{"all":90},"cod":200,"coord":{"lat":45.23,"lon":-122.8}}
  ```
  
- **/api/sun/{zip_code}/{country}** - current sunset/sunrise in city
  ```bash
  curl -X GET http://0.0.0.0:5001/sun/weather/97002/us
  ```
  _Response_: json object
  ```json
  {"astronomical_twilight_begin":"04:03:49 PM","astronomical_twilight_end":"04:29:50 AM"}
  ```

## Development notes

### CI/CD

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `mypy`, `pydocstyle`, `pylint`, `flake8`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-code.sh
```

Other than that, a fresh versioned package will be delivered on PYPI after new tag is created using [pythonpublish.yml](.github/workflows/pythonpublish.yml) file.

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request
