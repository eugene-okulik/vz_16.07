import pytest


ENV = 'prod'


@pytest.fixture(scope="session", autouse=True)
def get_args():
    config = {'env': 'TEST'}
    pytest.test_config = config
    return config


def pytest_sessionstart(session):
    print("Before tests")


def pytest_sessionfinish(session):
    print("After tests")


def pytest_runtest_setup(item):
    if 'db' in item.keywords and ENV == 'prod':
        pytest.skip("We don't want to run db tests")
