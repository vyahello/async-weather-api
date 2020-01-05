import flask

blueprint: flask.blueprints.Blueprint = flask.blueprints.Blueprint(__name__, __name__)


@blueprint.route("/")
def index() -> str:
    """Returns home page route."""
    return flask.render_template("index.html")


@blueprint.errorhandler(404)
def not_found() -> flask.Response:
    """Returns page not found."""
    return flask.Response("The page was not found", status=404)
