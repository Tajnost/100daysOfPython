import requests
from datetime import datetime

TOKEN = "gitg00d!23"
USERNAME = "vidgit"

today = datetime.today().strftime('%Y%m%d')
print(today)

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Created User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#Create Graph

#graph_config = {
#    "id": "graph1",
#    "name": "Geek Graph",
#    "unit": "Hours",
#    "type": "float",
#    "color": "ajisai",
#}



#response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
#print(response.json())

## ADDing stuff
quote = input("How many hours did you study? ")

print(quote)

addingStuff = {
    "date": today,
    "quantity": quote
}

response = requests.post(url=f"{graph_endpoint}/graph1", json=addingStuff, headers=headers)


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)