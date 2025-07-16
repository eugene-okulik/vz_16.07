import requests
from requests import JSONDecodeError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
    retry=retry_if_exception_type(JSONDecodeError))
def check_settings_saved(expected_value):
    response = requests.get('https://example.com')
    print("AAAAA")
    # response_json = response.json()
    response_json = {}
    assert response_json['my_setting'] == expected_value


@retry(stop=stop_after_attempt(10), wait=wait_fixed(10))
def check_setting(expected_value):
    print("Retrying")
    assert expected_value == 1


def test_setting():
    check_settings_saved(22)
