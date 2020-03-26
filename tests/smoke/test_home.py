from urequest.session import Session
from urequest.url import HttpUrl
from tests.markers import smoke
from weather import Bind

pytestmark = smoke


def test_index(http_session: Session, bind: Bind) -> None:
    assert http_session.get(url=HttpUrl(str(bind), "/index"))
