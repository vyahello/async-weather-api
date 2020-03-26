from urequest.session import Session
from urequest.url import HttpUrl
from tests.markers import smoke, async_

pytestmark = [smoke, async_]


def test_index(http_session: Session) -> None:
    assert http_session.get(url=HttpUrl("0.0.0.0:5000", "/index"))
