import  requests
import pytest


class SomeEndpoint:
    first_url, second_url = "http://test.expamle.com", "http://expamle.com"
    def get(self):
        if pytest.test_config['env'] == 'PROD':
            return print('requests.get(self.first_url)')
        else:
            return print('requests.get(self.second_url)')



def test_me():
    endp = SomeEndpoint()
    endp.get()