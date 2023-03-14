# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from app import index
def test_index():
    assert index() == "Hello, world!"
     