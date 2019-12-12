import os
from contextlib import contextmanager
from shutil import which

import pytest as pytest


@contextmanager
def null_context():
    yield


def find_binary(name: str) -> str:
    candidates = [
        os.environ.get('{}_BINARY', "".format(name.upper().replace("-", "_"))),
        name,
        "{}.exe".format(name),
    ]
    for candidate in candidates:
        path = which(candidate)
        if path:
            return path
    raise pytest.skip("Could not find driver {}, skipping".format(repr(name)))
