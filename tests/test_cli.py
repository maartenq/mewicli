# tests/test_main.py

import pytest
from mewicli.main import multipartify


@pytest.mark.parametrize(
    "incoming, converted",
    (
        ({"a": "b"}, {"a": "b"}),
        (
            {"a": {"Not", "serializable", "set"}},
            {"a": {"Not", "serializable", "set"}},
        ),
        ({"a": {"b1": "c", "b2": "d"}}, {"a[b1]": "c", "a[b2]": "d"}),
        ({"a": {"b": {"c": "d"}}}, {"a[b][c]": "d"}),
        ({"a": ["c", "e"]}, {"a[0]": "c", "a[1]": "e"}),
        ({"a": [{"b": "c"}, {"d": "e"}]}, {"a[0][b]": "c", "a[1][d]": "e"}),
        ({}, {}),
    ),
)
def test(incoming, converted):
    assert multipartify(incoming, formatter=lambda v: v) == converted


def test_default_formatter():
    assert multipartify({"a": "b"}) == {"a": (None, "b")}
