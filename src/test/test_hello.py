import requests
import pytest
#Initalize
message = {"hello"}

#Run
def hello():
    response = requests.get("http://localhost:5000/hello")
    responsejson = response.status_code
    return


def test_hello_code():
    assert hello() == "200"

