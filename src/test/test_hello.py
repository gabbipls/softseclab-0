import requests
#Initalize
message = {"hello"}

#Run
def test_hallo():
    response = requests.get("http://localhost:5000/hello")
    return response
response = test_hallo()
#Assert
responsejson = response.json()


assert responsejson['message'] == "200"