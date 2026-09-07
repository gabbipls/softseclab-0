import requests
import pytest
#Initalize
message = {"hello"}

#Run
def hello():
    response = requests.get("http://127.0.0.1:5000/hello")
    responsejson = response.status_code
    print(responsejson)
    return responsejson


def test_hello_code():
    assert hello() == 200

test_hello_code()
