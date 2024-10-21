import httpx

url = "https://literate-adventure-jj5gxxjjwj5w35rg6-5000.app.github.dev/"


#curl.exe -d "text=Hello!&param2=value2" -X POST "https://literate-adventure-jj5gxxjjwj5w35rg6-5000.app.github.dev/auth"
#curl.exe -d "id=william.french@uconn.edu&token=token123" -X POST https://literate-adventure-jj5gxxjjwj5w35rg6-5000.app.github.dev/auth
#curl.exe -d "id=william.french@uconn.edu&token=WrongToken" -X POST https://literate-adventure-jj5gxxjjwj5w35rg6-5000.app.github.dev/auth

response = httpx.get(url)
print(response.status_code)
print(response)



response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)

# Print the response
print(response.status_code)
print(response.text)  


authData = {
    "id": "william.french@uconn.edu",
    "token": "token123"
}

response = httpx.post(url + "auth", data=authData)

print(response.status_code)
print(response.text)  
