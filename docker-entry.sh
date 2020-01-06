#!/usr/bin/env bash

IMAGE_REPO="vyahello/async-weather-api"

helper() {
    cat <<HELP
    This script provides async weather REST API via docker.

    Please use next command:
      - 'help' to see tool help
         docker run ${IMAGE_REPO}:<image-version> --help
         ==================================================================================================================
      - 'weather' to run async weather REST API
         docker run -it -p <local-port>:<server-port> ${IMAGE_REPO}:<image-version> weather run --bind 0.0.0.0:<server-port>--mode prod --key <secret-key>

HELP
}


weather() {
    python -m weather $@
}


main() {
    if (
        [[ "$1" == "-h" ]] ||
        [[ "$1" == "--help" ]] ||
        [[ "$1" == "help" ]] ||
        [[ $# -eq 0 ]]
    ); then
        helper
        exit 0
    fi
    local cmd=$1; shift
    eval "${cmd} $@"
}


main $@