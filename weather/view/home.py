import quart

blueprint: quart.blueprints.Blueprint = quart.blueprints.Blueprint(
    __name__, __name__
)


@blueprint.route("/")
@blueprint.route("/index")
async def index() -> str:
    """Returns home page route."""
    return await quart.render_template("index.html")


@blueprint.errorhandler(404)
async def not_found() -> quart.Response:
    """Returns page not found."""
    return quart.Response("The page was not found", status=404)
