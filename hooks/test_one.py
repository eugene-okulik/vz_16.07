import pytest


def test_me():
    assert 1 == 1


@pytest.mark.db
def test_db(get_args):
    assert 1 == 1
