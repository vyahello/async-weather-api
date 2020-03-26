import _pytest.config.argparsing
import _pytest.fixtures
import pytest
from urequest.session import Session, HttpSession
from weather import Bind, run


def pytest_addoption(parser: _pytest.config.argparsing.Parser) -> None:
    """Adds `--key` (API) command line argument."""
    parser.addoption(
        "--key",
        action="store",
        help="Api key (openweathermap.org) for weather app e.g 'aazzvvbb11'",
        type=str,
        default="",
    )


@pytest.fixture(scope="session")
def weather_key(request: _pytest.fixtures.SubRequest) -> str:
    """Returns api key."""
    yield request.config.getoption("--key")


@pytest.fixture(scope="session")
def bind() -> Bind:
    """Returns bind address."""
    yield Bind()


@pytest.fixture
def startup_app(bind: Bind, weather_key: str) -> None:
    """Runs application."""
    run(weather_key, bind, debug=True)


@pytest.fixture(scope="session")
def http_session() -> Session:
    """Returns http session."""
    yield HttpSession()
