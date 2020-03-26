from tests.markers import unit
from weather import Bind

pytestmark = unit


def test_bind_host(bind: Bind) -> None:
    assert bind.host == "0.0.0.0"


def test_bind_port(bind: Bind) -> None:
    assert bind.port == 5000


def test_bind_as_str(bind: Bind) -> None:
    assert str(bind) == "0.0.0.0:5000"
