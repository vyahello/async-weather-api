#!/usr/bin/env bash

PACKAGE="weather"


--check-box() {
    printf "Start ${1} analysis ...\n"
}


remove-pycache() {
    ( find . -d -name __pycache__ | xargs rm -r )
}


check-black() {
    --check-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
    --check-box "flake" && ( flake8 ${PACKAGE} )
}


check-pylint() {
    --check-box "pylint" && ( pylint $(find ./ -iname *.py) )
}


check-mypy() {
    --check-box "mypy" && ( mypy --package "${PACKAGE}" )
}


check-pydocstyle() {
    --check-box "pydocstyle" && ( pydocstyle --explain --count ./ )
}


check-unittests() {
    --check-box "unitests" && pytest -m "unit or async_"
}


main() {
    remove-pycache
    check-black && \
    check-flake && \
    check-pylint && \
    check-mypy && \
    check-pydocstyle && \
    check-unittests
}


main
