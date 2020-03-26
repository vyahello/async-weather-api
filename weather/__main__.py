from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, _SubParsersAction
from typing import Dict, NamedTuple, Any
from weather import Bind, application
from weather.config import settings
from weather.services.weather import global_init


class _Arguments(NamedTuple):
    """Returns human-readable list of user's arguments."""

    bind: Bind
    debug: bool
    key: str
    mode: str
    command: str


def _arguments() -> _Arguments:
    """Returns list of user's arguments."""
    analytics_parser: ArgumentParser = ArgumentParser(
        description="The program allows to manipulate with async weather REST API",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    sub_parsers: _SubParsersAction = analytics_parser.add_subparsers(
        description="A list of allowed options for manipulation with async weather REST API.",
        help="It is allowed only to run async weather REST API.",
    )
    run_parser: ArgumentParser = sub_parsers.add_parser(name="run", help="Runs async weather rest API.")
    run_parser.set_defaults(command="run")
    run_parser.add_argument(
        "--bind",
        "-b",
        action="store",
        help="Socket address to launch app on e.g '0.0.0.0:5001'",
        type=str,
        default="0.0.0.0:5001",
    )
    run_parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable or disable debug option", default=False,
    )
    run_parser.add_argument(
        "--key",
        "-k",
        action="store",
        help="Api key (openweathermap.org) for weather app e.g 'aazzvvbb11'",
        type=str,
        required=True,
    )
    run_parser.add_argument(
        "--mode", "-m", action="store", help="Application mode for weather app e.g 'dev'", type=str, default="dev",
    )
    command_line_input: Dict[str, Any] = vars(analytics_parser.parse_args())
    if not command_line_input:
        analytics_parser.print_help()
        analytics_parser.exit(1)
    command_line_input["bind"] = Bind(*command_line_input["bind"].split(":"))
    return _Arguments(**command_line_input)


def _run_weather(arguments: _Arguments) -> None:
    """Runs weather app."""
    data = settings.load(arguments.mode)
    data["weather_key"] = arguments.key
    global_init(data["weather_key"])
    application.run(host=arguments.bind.host, port=int(arguments.bind.port), debug=arguments.debug)


if __name__ == "__main__":
    _run_weather(_arguments())
